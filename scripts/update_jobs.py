import json
import os
import requests

# -------------------------------
# 模拟抓取职位
# -------------------------------
jobs = [
    {"title":"Python 数据标注员", "company":"OpenAI", "location":"Remote", "url":"https://example.com/job1", "source":"手动添加"},
    {"title":"AI 内容审核", "company":"DeepMind", "location":"Remote", "url":"https://example.com/job2", "source":"手动添加"}
]

# -------------------------------
# 历史职位去重
# -------------------------------
jobs_file = "../jobs/jobs.json"
if not os.path.exists(jobs_file):
    history = []
else:
    with open(jobs_file, "r", encoding="utf-8") as f:
        history = json.load(f)

new_jobs = []
for job in jobs:
    if job["url"] not in [h["url"] for h in history]:
        new_jobs.append(job)
        history.append(job)

# -------------------------------
# 保存历史职位
# -------------------------------
os.makedirs(os.path.dirname(jobs_file), exist_ok=True)
with open(jobs_file, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=2)

print(f"✅ 本次新增职位数量: {len(new_jobs)}")

# -------------------------------
# Telegram 推送
# -------------------------------
def send_telegram(job):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("⚠️ Telegram token or chat_id not set")
        return
    text = f"🔥 New Job\n\nCompany: {job['company']}\nPosition: {job['title']}\nLocation: {job['location']}\nLink: {job['url']}\nSource: {job['source']}"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(url, params={"chat_id": chat_id, "text": text})

for job in new_jobs:
    send_telegram(job)
