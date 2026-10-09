"""Build every derived artifact of the OpenJobs site from ``public/jobs.json``.

``public/jobs.json`` is the single source of truth. Running this script
regenerates:

* ``public/stats.json``      – aggregate statistics shown on the site
* ``public/sitemap.xml``     – sitemap for search engines
* ``public/rss.xml``         – RSS feed of the latest jobs
* ``public/jobs/*.html``     – one detail page per locally hosted job
* ``README.md``              – latest-jobs table for the GitHub homepage

Usage:  python scripts/build_site.py
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
JOBS_FILE = PUBLIC / "jobs.json"
DETAIL_DIR = PUBLIC / "jobs"
README_FILE = ROOT / "README.md"

SITE_URL = "https://openjobs.genedai.me"
SITE_NAME = "OpenJobs"
README_JOB_LIMIT = 20
RSS_ITEM_LIMIT = 50
REQUIRED_FIELDS = ("company", "title", "location", "url")

# Keep in sync with getJobCategory() in public/index.html.
CATEGORY_RULES = [
    ("AI", re.compile(r"\b(ai|ml|machine learning|data scientist|llm)\b", re.I)),
    ("DevOps", re.compile(r"\b(devops|sre|infrastructure|platform)\b", re.I)),
    ("SEO", re.compile(r"\b(seo|marketing|content)\b", re.I)),
    (
        "Developer",
        re.compile(
            r"\b(frontend|backend|fullstack|full stack|python|software|engineer|developer)\b",
            re.I,
        ),
    ),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def atomic_write(path: Path, content: str) -> None:
    """Write text via a temp file + rename so an interrupted run never leaves
    a truncated file behind."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def category_of(title: str) -> str:
    for name, pattern in CATEGORY_RULES:
        if pattern.search(title):
            return name
    return "Other"


def is_local(url: str) -> bool:
    return not re.match(r"^[a-z]+://", url) and url.startswith("jobs/")


def abs_url(url: str) -> str:
    """Absolute URL for a job link (feeds and sitemap need absolute URLs)."""
    if re.match(r"^[a-z]+://", url):
        return url
    return f"{SITE_URL}/{url.lstrip('/')}"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_jobs(path: Path = JOBS_FILE) -> list[dict]:
    """Load, validate, normalise and de-duplicate jobs."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"{path} must contain a JSON array")

    seen: set[str] = set()
    jobs: list[dict] = []
    for idx, item in enumerate(raw):
        if not isinstance(item, dict):
            print(f"skip #{idx}: not an object", file=sys.stderr)
            continue
        job = {k: str(item.get(k, "")).strip() for k in REQUIRED_FIELDS}
        missing = [k for k in REQUIRED_FIELDS if not job[k]]
        if missing:
            print(f"skip #{idx}: missing {', '.join(missing)}", file=sys.stderr)
            continue
        if job["url"] in seen:
            continue
        seen.add(job["url"])
        for optional in ("apply_url", "posted_at", "source"):
            if item.get(optional):
                job[optional] = str(item[optional]).strip()
        jobs.append(job)

    jobs.sort(key=lambda j: (j["company"].lower(), j["title"].lower(), j["url"]))
    return jobs


def build_stats(jobs: list[dict], now: datetime) -> dict:
    companies = Counter(j["company"] for j in jobs)
    return {
        "total_jobs": len(jobs),
        "total_companies": len(companies),
        "total_locations": len({j["location"] for j in jobs}),
        "top_companies": dict(companies.most_common(10)),
        "categories": dict(Counter(category_of(j["title"]) for j in jobs)),
        "top_locations": dict(Counter(j["location"] for j in jobs).most_common(10)),
        "updated_at": now.isoformat(timespec="seconds"),
    }


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

DETAIL_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {company} - {site}</title>
<meta name="description" content="{title}，{company}，地点：{location}。">
<link rel="canonical" href="{canonical}">
<style>
  :root {{ --bg:#0f172a; --card:#1e293b; --border:#334155; --text:#f8fafc; --muted:#94a3b8; --primary:#6366f1; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;
         background:var(--bg); color:var(--text); line-height:1.6; min-height:100vh; }}
  main {{ max-width:760px; margin:0 auto; padding:3rem 1.5rem; }}
  a {{ color:var(--primary); }}
  .back {{ color:var(--muted); text-decoration:none; font-size:.9rem; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:2rem; margin-top:1.5rem; }}
  h1 {{ font-size:clamp(1.5rem,4vw,2rem); margin-bottom:.5rem; }}
  .meta {{ color:var(--muted); display:flex; gap:1rem; flex-wrap:wrap; }}
  .tag {{ background:rgba(99,102,241,.12); color:#a5b4fc; padding:.25rem .6rem; border-radius:6px; font-size:.8rem; }}
  .btn {{ display:inline-block; margin-top:1.5rem; padding:.8rem 1.6rem; border-radius:10px;
         background:linear-gradient(135deg,#6366f1,#8b5cf6 50%,#ec4899); color:#fff; font-weight:600; text-decoration:none; }}
  .note {{ color:var(--muted); font-size:.85rem; margin-top:1.5rem; }}
</style>
</head>
<body>
<main>
  <a class="back" href="../">← 返回职位列表</a>
  <div class="card">
    <div class="meta"><span>{company}</span><span>📍 {location}</span><span class="tag">{category}</span></div>
    <h1 style="margin-top:.75rem">{title}</h1>
    {apply}
    <p class="note">职位信息由 OpenJobs 整理，请以公司官网的最新信息为准。</p>
  </div>
</main>
</body>
</html>
"""


def render_detail(job: dict) -> str:
    apply_html = ""
    if job.get("apply_url"):
        apply_html = (
            f'<a class="btn" href="{esc(job["apply_url"])}" target="_blank" '
            f'rel="noopener noreferrer">前往申请</a>'
        )
    return DETAIL_TEMPLATE.format(
        title=esc(job["title"]),
        company=esc(job["company"]),
        location=esc(job["location"]),
        category=esc(category_of(job["title"])),
        site=esc(SITE_NAME),
        canonical=esc(abs_url(job["url"])),
        apply=apply_html,
    )


def write_detail_pages(jobs: list[dict]) -> int:
    """Write detail pages for local jobs and remove stale ones."""
    wanted: set[str] = set()
    count = 0
    for job in jobs:
        if not is_local(job["url"]):
            continue
        target = PUBLIC / job["url"]
        wanted.add(target.name)
        atomic_write(target, render_detail(job))
        count += 1

    if DETAIL_DIR.exists():
        for old in DETAIL_DIR.glob("*.html"):
            if old.name not in wanted:
                old.unlink()
    return count


def render_readme(jobs: list[dict], now: datetime) -> str:
    def link(job: dict) -> str:
        return job["url"] if not is_local(job["url"]) else f"public/{job['url']}"

    lines = [
        "# 🚀 AI Remote Jobs Daily",
        "",
        f"Last Update: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "",
        f"Total: **{len(jobs)}** jobs from **{len({j['company'] for j in jobs})}** companies.",
        "",
        "## 🔥 Latest Remote Jobs",
        "",
        "| Company | Position | Location |",
        "|---|---|---|",
    ]
    for job in jobs[:README_JOB_LIMIT]:
        lines.append(
            f"| {job['company']} | [{job['title']}]({link(job)}) | {job['location']} |"
        )
    lines += [
        "",
        "---",
        "",
        "## 🌍 About",
        "",
        "This site updates remote jobs automatically with GitHub Actions. "
        "The web app lives in [`public/`](public/).",
        "",
        "## 🛠 Development",
        "",
        "```bash",
        "python scripts/build_site.py   # rebuild all generated files",
        "python scripts/update_jobs.py  # fetch new jobs, then rebuild",
        "```",
        "",
    ]
    return "\n".join(lines)


def render_sitemap(jobs: list[dict], now: datetime) -> str:
    today = now.strftime("%Y-%m-%d")
    urls = [(f"{SITE_URL}/", "hourly", "1.0")]
    urls += [(abs_url(j["url"]), "weekly", "0.6") for j in jobs if is_local(j["url"])]
    body = "\n".join(
        f"  <url>\n    <loc>{esc(loc)}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for loc, freq, prio in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n"
    )


def render_rss(jobs: list[dict], now: datetime) -> str:
    items = []
    for job in jobs[:RSS_ITEM_LIMIT]:
        link = abs_url(job["url"])
        items.append(
            "    <item>\n"
            f"      <title>{esc(job['title'])} at {esc(job['company'])}</title>\n"
            f"      <link>{esc(link)}</link>\n"
            f"      <guid isPermaLink=\"true\">{esc(link)}</guid>\n"
            f"      <description>{esc(job['location'])}</description>\n"
            f"      <category>{esc(category_of(job['title']))}</category>\n"
            f"      <pubDate>{format_datetime(now)}</pubDate>\n"
            "    </item>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n  <channel>\n'
        f"    <title>{esc(SITE_NAME)} - Remote Job Openings</title>\n"
        f"    <link>{SITE_URL}/</link>\n"
        f"    <description>Latest remote job openings ({len(jobs)} total).</description>\n"
        "    <language>zh-cn</language>\n"
        f"    <lastBuildDate>{format_datetime(now)}</lastBuildDate>\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build(now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    jobs = load_jobs()

    atomic_write(PUBLIC / "stats.json", json.dumps(build_stats(jobs, now), ensure_ascii=False, indent=2) + "\n")
    atomic_write(PUBLIC / "sitemap.xml", render_sitemap(jobs, now))
    atomic_write(PUBLIC / "rss.xml", render_rss(jobs, now))
    detail_count = write_detail_pages(jobs)
    atomic_write(README_FILE, render_readme(jobs, now))

    print(f"built site: {len(jobs)} jobs, {detail_count} detail pages")
    return {"jobs": len(jobs), "detail_pages": detail_count}


if __name__ == "__main__":
    build()
