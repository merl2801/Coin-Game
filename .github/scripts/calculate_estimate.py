import os
import requests
import re

token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("REPO")
issue_number = os.getenv("ISSUE_NUMBER")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

owner, repo_name = repo.split("/")

# Lấy tất cả issues có label log/work-time
issues_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
all_issues = requests.get(issues_url, headers=headers, params={"state": "open", "per_page": 100}).json()

total_minutes = 0

for issue in all_issues:
    body = issue.get("body", "")
    # Tìm field "Issue" (issue_id)
    m = re.search(r"Issue.*?(\d+)", body)
    if m and m.group(1) == str(issue_number):
        # Tìm thời gian (h hoặc m)
        t = re.search(r"作業時間.*?(\d+(?:\.\d+)?)", body)
        if t:
            hours = float(t.group(1))
            total_minutes += int(hours * 60)

# Tính tổng giờ phút
hours = total_minutes // 60
minutes = total_minutes % 60
total_time = f"{hours}h {minutes}m"

# Gửi comment vào issue cha
comment_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{issue_number}/comments"
comment_body = {"body": f"⏱ **Tổng thời gian** từ các sub-issues: **{total_time}**"}
requests.post(comment_url, headers=headers, json=comment_body)

print(f"Tổng thời gian: {total_time}")
