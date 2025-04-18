import re

with open("../NafisDailyGrind/logs/daily-log.md", "r") as f:
    log_data = f.read()

# Extract all date blocks
log_blocks = re.findall(r"## ✅ \d{4}-\d{2}-\d{2}.*?(?=## ✅|\Z)", log_data, re.DOTALL)

# Keep only last 5 entries
latest_logs = log_blocks[:5]

# Format for profile
formatted = "## 📅 Latest Logs from NafisDailyGrind\n\n```\n" + "\n---\n".join([log.strip() for log in latest_logs]) + "\n```"

# Inject into README
with open("README.md", "r") as f:
    readme = f.read()

updated = re.sub(r"## 📅 Latest Logs from NafisDailyGrind[\s\S]+?```", formatted, readme)

with open("README.md", "w") as f:
    f.write(updated)

print("✅ README updated with latest logs.")
