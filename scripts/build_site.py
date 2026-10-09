"""Build every derived artifact of the OpenJobs site from ``public/jobs.json``.

``public/jobs.json`` is the single source of truth. Each job is an object:

    required  company, title, location, url
    optional  salary        e.g. "8-13K"           (shown as-is, never invented)
              tags          e.g. ["辅导老师"]
              industry      e.g. "教育培训"
              added_at      ISO date the job entered this site (YYYY-MM-DD)
              description   list of bullet strings or a single string
              apply_url     external link to the original posting

``url`` is either an absolute ``https://`` link to the original posting or a
path relative to ``public/`` (e.g. ``jobs/openai-ai-engineer.html``) for
jobs that have an on-site detail page.

Generated files:

* ``public/stats.json``           aggregate statistics
* ``public/sitemap.xml``          sitemap (home, categories, detail pages)
* ``public/rss.xml``              RSS feed of the latest jobs
* ``public/jobs/*.html``          detail page per locally hosted job
* ``public/categories/*.html``    crawlable landing page per category
* ``README.md``                   latest-jobs table for the GitHub homepage

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

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
JOBS_FILE = PUBLIC / "jobs.json"
DETAIL_DIR = PUBLIC / "jobs"
CATEGORY_DIR = PUBLIC / "categories"
README_FILE = ROOT / "README.md"

SITE_URL = "https://openjobs.genedai.me"
SITE_NAME = "OpenJobs"
SUBMIT_URL = "https://github.com/ceecee1234/openjobs/issues/new?template=job_submission.md"
REPO_URL = "https://github.com/ceecee1234/openjobs"
README_JOB_LIMIT = 20
RSS_ITEM_LIMIT = 50
REQUIRED_FIELDS = ("company", "title", "location", "url")
OPTIONAL_TEXT_FIELDS = ("salary", "industry", "apply_url", "added_at")

# Keep in sync with CATEGORIES in public/index.html. Order matters: the first
# match wins, so specific roles (DevOps, SEO) must come before the generic
# "engineer"/"developer" rule.
# (key, slug, Chinese label, pattern)
CATEGORIES = [
    ("AI", "ai", "AI 相关", re.compile(r"\b(ai|ml|machine learning|data scientist|llm)\b", re.I)),
    ("DevOps", "devops", "DevOps", re.compile(r"\b(devops|sre|infrastructure|platform)\b", re.I)),
    ("SEO", "seo", "SEO / 营销", re.compile(r"\b(seo|marketing|content)\b", re.I)),
    ("Developer", "developer", "开发者", re.compile(
        r"\b(frontend|backend|fullstack|full stack|python|software|engineer|developer)\b", re.I)),
    ("Other", "other", "其他", None),
]
CATEGORY_LABEL = {key: label for key, _, label, _ in CATEGORIES}
CATEGORY_SLUG = {key: slug for key, slug, _, _ in CATEGORIES}

CSS_BASE = """
:root{--bg:#0f172a;--card:#1e293b;--card2:#273449;--border:#334155;--text:#f8fafc;--muted:#94a3b8;--primary:#6366f1;--accent:#a5b4fc;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);line-height:1.7;min-height:100vh}
a{color:var(--accent)}
.wrap{max-width:860px;margin:0 auto;padding:0 1.25rem}
header{border-bottom:1px solid var(--border);background:rgba(15,23,42,.9)}
header .wrap{display:flex;justify-content:space-between;align-items:center;height:60px}
.brand{color:var(--text);text-decoration:none;font-weight:700}
nav a{color:var(--muted);text-decoration:none;margin-left:1.2rem;font-size:.9rem}
main{padding:2.5rem 0 3rem}
.crumbs{font-size:.85rem;color:var(--muted)}
.crumbs a{color:var(--muted)}
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1.75rem;margin-top:1.25rem}
h1{font-size:clamp(1.5rem,4vw,2rem);font-weight:800;line-height:1.3}
.meta{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:.9rem}
.tag{font-size:.8rem;padding:.25rem .6rem;border-radius:6px;background:rgba(99,102,241,.14);color:var(--accent)}
.tag.salary{background:rgba(34,197,94,.14);color:#86efac}
.tag.loc{background:rgba(14,165,233,.14);color:#7dd3fc}
h2{font-size:1.05rem;margin:1.5rem 0 .6rem}
ul.bullets{padding-left:1.2rem;color:#cbd5e1}
ul.bullets li{margin:.3rem 0}
.btn{display:inline-block;margin-top:1.4rem;padding:.8rem 1.6rem;border-radius:10px;background:linear-gradient(135deg,#6366f1,#8b5cf6 50%,#ec4899);color:#fff;font-weight:600;text-decoration:none}
.note{color:var(--muted);font-size:.85rem;margin-top:1.5rem}
.related{list-style:none;padding:0}
.related li{border-top:1px solid var(--border);padding:.7rem 0}
.related a{color:var(--text);text-decoration:none;font-weight:600}
.related small{color:var(--muted);display:block}
footer{border-top:1px solid var(--border);padding:1.5rem 0;color:var(--muted);font-size:.8rem;text-align:center}
footer a{color:var(--muted)}
"""


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
    for key, _, _, pattern in CATEGORIES:
        if pattern is not None and pattern.search(title):
            return key
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


def normalise_description(value: object) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [line.strip("-• ").strip() for line in value.splitlines() if line.strip()]
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    return []


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
        for key in OPTIONAL_TEXT_FIELDS:
            if item.get(key):
                job[key] = str(item[key]).strip()
        job["tags"] = [str(t).strip() for t in item.get("tags", []) if str(t).strip()]
        job["description"] = normalise_description(item.get("description"))
        job["category"] = category_of(job["title"])
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
        "categories": dict(Counter(j["category"] for j in jobs)),
        "top_locations": dict(Counter(j["location"] for j in jobs).most_common(10)),
        "updated_at": now.isoformat(timespec="seconds"),
    }


def page_shell(title: str, description: str, canonical: str, body: str,
               crumbs: list[tuple[str, str]], extra_head: str = "", root: str = "../") -> str:
    """Common HTML shell for detail and category pages.

    ``root`` is the relative path from the page to ``public/`` root.
    """
    header = (
        f'<header><div class="wrap"><a class="brand" href="{root}">🚀 AI Remote Jobs</a>'
        f'<nav><a href="{root}#jobs">职位</a><a href="{root}categories/ai.html">AI 职位</a>'
        f'<a href="{SUBMIT_URL}" target="_blank" rel="noopener noreferrer">投稿职位</a>'
        f'<a href="{root}rss.xml">RSS</a></nav></div></header>'
    )
    crumb_html = " / ".join(
        f'<a href="{esc(href)}">{esc(label)}</a>' if href else esc(label) for label, href in crumbs
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} · {SITE_NAME}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{esc(canonical)}">
<meta name="robots" content="index,follow">
<link rel="alternate" type="application/rss+xml" title="{SITE_NAME} RSS" href="{root}rss.xml">
<style>{CSS_BASE}</style>
{extra_head}
</head>
<body>
{header}
<main class="wrap">
  <div class="crumbs">{crumb_html}</div>
{body}
</main>
<footer><div class="wrap">职位信息收集自网络，仅供参考，请以公司官网和原始发布为准 · <a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">GitHub</a></div></footer>
</body>
</html>
"""


def job_card_html(job: dict, root: str) -> str:
    """Compact related-job item used on detail pages."""
    href = job["url"] if not is_local(job["url"]) else f"{root}{job['url']}"
    return (
        f'<li><a href="{esc(href)}">{esc(job["title"])}</a>'
        f'<small>{esc(job["company"])} · {esc(job["location"])}'
        f'{" · " + esc(job["salary"]) if job.get("salary") else ""}</small></li>'
    )


def json_ld_job_posting(job: dict) -> str:
    """schema.org JobPosting (only when we have a real description to offer)."""
    if not job["description"]:
        return ""
    data = {
        "@context": "https://schema.org",
        "@type": "JobPosting",
        "title": job["title"],
        "description": "<ul>" + "".join(f"<li>{esc(d)}</li>" for d in job["description"]) + "</ul>",
        "hiringOrganization": {"@type": "Organization", "name": job["company"]},
        "jobLocation": {"@type": "Place", "address": job["location"]},
        "url": abs_url(job["url"]),
    }
    if job.get("added_at"):
        data["datePosted"] = job["added_at"]
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def render_detail(job: dict, jobs: list[dict]) -> str:
    root = "../"
    meta = [f'<span class="tag">{esc(CATEGORY_LABEL[job["category"]])}</span>',
            f'<span class="tag loc">📍 {esc(job["location"])}</span>']
    if job.get("salary"):
        meta.insert(0, f'<span class="tag salary">💰 {esc(job["salary"])}</span>')
    meta += [f'<span class="tag">#{esc(t)}</span>' for t in job["tags"]]

    if job["description"]:
        desc = ('<h2>职位描述</h2><ul class="bullets">'
                + "".join(f"<li>{esc(d)}</li>" for d in job["description"]) + "</ul>")
    else:
        desc = ('<h2>职位描述</h2><p style="color:var(--muted)">我们暂未整理该职位的详细描述，'
                '请点击下方按钮查看原始发布。</p>')

    apply_url = job.get("apply_url") or (job["url"] if not is_local(job["url"]) else "")
    apply_html = (f'<a class="btn" href="{esc(apply_url)}" target="_blank" rel="noopener noreferrer">'
                  f'前往申请 →</a>') if apply_url else ""

    same_company = [j for j in jobs if j["company"] == job["company"] and j is not job][:5]
    same_cat = [j for j in jobs if j["category"] == job["category"]
                and j["company"] != job["company"] and j is not job][:5]

    related = ""
    if same_company:
        related += ('<div class="card"><h2 style="margin-top:0">同公司其他职位</h2><ul class="related">'
                    + "".join(job_card_html(j, root) for j in same_company) + "</ul></div>")
    if same_cat:
        related += ('<div class="card"><h2 style="margin-top:0">相似方向的职位</h2><ul class="related">'
                    + "".join(job_card_html(j, root) for j in same_cat) + "</ul></div>")

    body = f"""  <div class="card">
    <h1>{esc(job['title'])}</h1>
    <p style="margin-top:.4rem;color:var(--muted)">{esc(job['company'])}{(' · 收录于 ' + esc(job['added_at'])) if job.get('added_at') else ''}</p>
    <div class="meta">{''.join(meta)}</div>
    {desc}
    {apply_html}
    <p class="note">本页信息由 OpenJobs 收集整理，可能存在遗漏或过期，请以原始发布为准。</p>
  </div>
  {related}"""

    return page_shell(
        title=f"{job['title']} · {job['company']}",
        description=f"{job['company']} 招聘 {job['title']}，地点 {job['location']}。{'薪资 ' + job['salary'] + '。' if job.get('salary') else ''}",
        canonical=abs_url(job["url"]),
        body=body,
        crumbs=[("首页", root), (job["company"], ""), (job["title"], "")],
        extra_head=json_ld_job_posting(job),
        root=root,
    )


def render_category(key: str, jobs: list[dict]) -> str:
    root = "../"
    label = CATEGORY_LABEL[key]
    items = [j for j in jobs if j["category"] == key]
    rows = []
    for j in items:
        href = j["url"] if not is_local(j["url"]) else f"{root}{j['url']}"
        rows.append(
            f'<li><a href="{esc(href)}">{esc(j["title"])}</a>'
            f'<small>{esc(j["company"])} · {esc(j["location"])}'
            f'{" · " + esc(j["salary"]) if j.get("salary") else ""}</small></li>'
        )
    body = f"""  <h1 style="margin-top:.75rem">{esc(label)}远程职位</h1>
  <p style="color:var(--muted);margin-top:.5rem">共收录 {len(items)} 个{esc(label)}方向的远程职位，每日更新。</p>
  <div class="card"><ul class="related">{''.join(rows) or '<li>暂无职位</li>'}</ul></div>
  <p class="note"><a href="{root}">← 查看全部职位</a></p>"""
    return page_shell(
        title=f"{label}远程职位",
        description=f"收录 {len(items)} 个{label}方向的远程职位，来自知名科技公司。",
        canonical=f"{SITE_URL}/categories/{CATEGORY_SLUG[key]}.html",
        body=body,
        crumbs=[("首页", root), (label, "")],
        root=root,
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
        atomic_write(target, render_detail(job, jobs))
        count += 1
    if DETAIL_DIR.exists():
        for old in DETAIL_DIR.glob("*.html"):
            if old.name not in wanted:
                old.unlink()
    return count


def write_category_pages(jobs: list[dict]) -> list[str]:
    written = []
    for key, slug, _, _ in CATEGORIES:
        if not any(j["category"] == key for j in jobs):
            continue
        atomic_write(CATEGORY_DIR / f"{slug}.html", render_category(key, jobs))
        written.append(slug)
    return written


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
        lines.append(f"| {job['company']} | [{job['title']}]({link(job)}) | {job['location']} |")
    lines += [
        "",
        "Browse everything on the website in [`public/`](public/), or subscribe via [RSS](public/rss.xml).",
        "",
        "## 📮 Submit a job",
        "",
        f"Found a remote job we should list? [Open a submission issue]({SUBMIT_URL}).",
        "",
        "---",
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


def render_sitemap(jobs: list[dict], now: datetime, categories: list[str]) -> str:
    today = now.strftime("%Y-%m-%d")
    urls = [(f"{SITE_URL}/", "hourly", "1.0")]
    urls += [(f"{SITE_URL}/categories/{slug}.html", "daily", "0.8") for slug in categories]
    urls += [(abs_url(j["url"]), "weekly", "0.6") for j in jobs if is_local(j["url"])]
    body = "\n".join(
        f"  <url>\n    <loc>{esc(loc)}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for loc, freq, prio in urls
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{body}\n</urlset>\n")


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
            f"      <category>{esc(CATEGORY_LABEL[job['category']])}</category>\n"
            f"      <pubDate>{format_datetime(now)}</pubDate>\n"
            "    </item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0">\n  <channel>\n'
            f"    <title>{esc(SITE_NAME)} - Remote Job Openings</title>\n"
            f"    <link>{SITE_URL}/</link>\n"
            f"    <description>Latest remote job openings ({len(jobs)} total).</description>\n"
            "    <language>zh-cn</language>\n"
            f"    <lastBuildDate>{format_datetime(now)}</lastBuildDate>\n"
            + "\n".join(items)
            + "\n  </channel>\n</rss>\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build(now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    jobs = load_jobs()

    atomic_write(PUBLIC / "stats.json",
                 json.dumps(build_stats(jobs, now), ensure_ascii=False, indent=2) + "\n")
    detail_count = write_detail_pages(jobs)
    categories = write_category_pages(jobs)
    atomic_write(PUBLIC / "sitemap.xml", render_sitemap(jobs, now, categories))
    atomic_write(PUBLIC / "rss.xml", render_rss(jobs, now))
    atomic_write(README_FILE, render_readme(jobs, now))

    print(f"built site: {len(jobs)} jobs, {detail_count} detail pages, {len(categories)} category pages")
    return {"jobs": len(jobs), "detail_pages": detail_count, "categories": categories}


if __name__ == "__main__":
    build()
