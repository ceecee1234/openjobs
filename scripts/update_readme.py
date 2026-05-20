from datetime import datetime
import random
import os

companies = [
    "OpenAI",
    "GitLab",
    "Zapier",
    "Automattic",
    "Cloudflare",
    "Notion",
    "Stripe",
    "Shopify"
]

positions = [
    "AI Engineer",
    "Frontend Developer",
    "Backend Developer",
    "Python Developer",
    "DevOps Engineer",
    "SEO Specialist"
]

locations = [
    "Remote",
    "Worldwide",
    "USA",
    "Europe",
    "Asia"
]

descriptions = [
    "Work with AI systems and build scalable products.",
    "Build modern frontend applications.",
    "Develop APIs and backend services.",
    "Manage cloud infrastructure and DevOps.",
    "Create SEO content and optimize websites."
]

# 创建 jobs 文件夹
os.makedirs("jobs", exist_ok=True)

# 首页 README
content = f"# 🚀 AI Remote Jobs Daily\n\n"
content += f"Last Update: {datetime.utcnow()} UTC\n\n"

content += "## 🔥 Latest Remote Jobs\n\n"

content += "| Company | Position | Location |\n"
content += "|---|---|---|\n"

# 生成职位
for i in range(20):

    company = random.choice(companies)
    position = random.choice(positions)
    location = random.choice(locations)
    description = random.choice(descriptions)

    slug = f"{company}-{position}".lower().replace(" ", "-")

    # 详情页文件名
    job_file = f"jobs/{slug}.html"

    # 写入职位详情页
    job_html = f"""
    <html>
    <head>
        <title>{position} at {company}</title>
    </head>
    <body style="font-family: Arial; padding:40px; max-width:800px; margin:auto;">
        <h1>{position}</h1>

        <h2>{company}</h2>

        <p><strong>Location:</strong> {location}</p>

        <h3>Job Description</h3>

        <p>{description}</p>

        <h3>Requirements</h3>

        <ul>
            <li>Remote work experience preferred</li>
            <li>English communication skills</li>
            <li>AI tools experience is a plus</li>
        </ul>

        <h3>Salary</h3>

        <p>$80,000 - $150,000 USD</p>

        <h3>Apply</h3>

        <a href="https://remoteok.com/" target="_blank">
            Apply Here
        </a>

    </body>
    </html>
    """

    with open(job_file, "w", encoding="utf-8") as f:
        f.write(job_html)

    # README 添加链接
    content += f"| {company} | [{position}]({job_file}) | {location} |\n"

# README 尾部
content += "\n---\n"

content += """
## 🌍 About

This website automatically updates remote jobs every few hours using GitHub Actions.

## 📩 Telegram Channel

Coming Soon...
"""

# 写入 README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Jobs generated successfully")
