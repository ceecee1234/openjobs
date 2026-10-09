# Job leads

Raw leads that need review or a source link before they can be published.

- Each file is `{"_meta": {...}, "leads": [...], "excluded": [...]}`.
- A lead is **published** only when it has a non-empty `url`
  (`scripts/update_jobs.py` → `load_leads()`).
- Leads with `"url": null` are kept for follow-up and are **never** published,
  and no link is ever generated for them.
- `excluded` records why an item was dropped (not a job, grey-market risk,
  off-scope location, etc.) so decisions can be audited.

Fields: `title`, `company`, `location`, `job_type`, `score`, `source`, `url`,
`status`, `notes`.
