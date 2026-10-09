"""Fetch new jobs, merge them into ``public/jobs.json`` and rebuild the site.

Pipeline:
  1. ``fetch_new_jobs()`` collects candidate jobs from the configured sources.
  2. New jobs (by URL) are appended to ``public/jobs.json``.
  3. Each new job is announced on Telegram if credentials are configured.
  4. ``build_site.build()`` regenerates every derived file.

Environment variables (optional):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID  – enable Telegram notifications.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site  # noqa: E402  (needs the sys.path tweak above)

TELEGRAM_TIMEOUT = 10  # seconds
SOURCES: list = []  # add fetcher callables here: each returns list[dict]


def fetch_new_jobs() -> list[dict]:
    """Collect candidate jobs from every registered source.

    No live source is wired up yet, so this returns nothing and the job
    list is left unchanged. Add a fetcher to ``SOURCES`` to enable one.
    """
    candidates: list[dict] = []
    for source in SOURCES:
        try:
            candidates.extend(source())
        except Exception as exc:  # one broken source must not stop the run
            print(f"⚠️ source {getattr(source, '__name__', source)} failed: {exc}", file=sys.stderr)
    return candidates


def merge(existing: list[dict], candidates: list[dict]) -> list[dict]:
    """Return the jobs that are new (by URL) and not already stored."""
    known = {j["url"] for j in existing}
    new_jobs: list[dict] = []
    for job in candidates:
        url = str(job.get("url", "")).strip()
        if url and url not in known:
            known.add(url)
            new_jobs.append(job)
    return new_jobs


def notify_telegram(job: dict) -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    text = (
        "🔥 New Job\n\n"
        f"Company: {job['company']}\n"
        f"Position: {job['title']}\n"
        f"Location: {job['location']}\n"
        f"Link: {job['url']}"
    )
    # Token is sent in the URL path as required by the Bot API; never log it.
    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": text, "disable_web_page_preview": True},
            timeout=TELEGRAM_TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"⚠️ Telegram notification failed for {job['url']}: {type(exc).__name__}", file=sys.stderr)


def main() -> int:
    jobs_file = build_site.JOBS_FILE
    existing = build_site.load_jobs(jobs_file) if jobs_file.exists() else []

    new_jobs = merge(existing, fetch_new_jobs())
    print(f"✅ new jobs this run: {len(new_jobs)}")
    if not new_jobs:
        # Nothing changed: skip the rebuild so generated files (which embed
        # timestamps) stay byte-identical and no empty commit is created.
        return 0

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for job in new_jobs:
        job.setdefault("added_at", today)

    combined = existing + new_jobs
    build_site.atomic_write(jobs_file, json.dumps(combined, ensure_ascii=False, indent=2) + "\n")

    for job in new_jobs:
        notify_telegram(job)

    build_site.build()
    return 0


if __name__ == "__main__":
    sys.exit(main())
