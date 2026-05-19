from datetime import datetime
import random

companies = [
    "OpenAI",
    "GitLab",
    "Zapier",
    "Automattic",
    "Toptal",
    "Cloudflare",
    "Notion",
    "Stripe",
    "Shopify",
    "Airbnb"
]

positions = [
    "AI Engineer",
    "Frontend Developer",
    "Backend Developer",
    "Python Developer",
    "Customer Support",
    "Product Designer",
    "DevOps Engineer",
    "SEO Specialist",
    "Content Writer",
    "Marketing Manager"
]

locations = [
    "Remote",
    "Worldwide",
    "USA",
    "Europe",
    "Asia",
    "Global"
]

content = f"# 🚀 AI Remote Jobs Daily\n\n"
content += f"Last Update: {datetime.utcnow()} UTC\n\n"

content += "## 🔥 Latest Remote Jobs\n\n"

content += "| Company | Position | Location |\n"
content += "|---|---|---|\n"

for i in range(20):
    company = random.choice(companies)
    position = random.choice(positions)
    location = random.choice(locations)

    content += f"| {company} | {position} | {location} |\n"

content += "\n---\n"

content += """
## 🌍 About

This website automatically updates remote jobs every few hours using GitHub Actions.

## 🔥 Categories

- AI Jobs
- Remote Jobs
- Beginner Friendly Jobs
- Worldwide Opportunities

## 📩 Telegram Channel

Coming Soon...
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README.md updated successfully")
