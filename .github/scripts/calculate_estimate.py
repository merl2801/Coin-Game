import os
import requests
import re

token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("REPO")
issue_number = os.getenv("ISSUE_NUMBER")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.mockingbird-preview+json"
}

owner, repo_name = repo.split("/")

# Lấy các sự kiện timeline để tìm linked issues
timeline_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{issue_number}/timeline"
timeline_res = requests.get(timeline_url, headers=headers)
timeline_data = timeline_res.json()

linked_issues = [
    event["source"]["issue"]["number"]
    for event in timeline_data
    if event.get("event") == "cross-referenced" and "issue" in event.get("source", {})
]

total_minutes = 0

for sub_issue_number in linked_issues:
    issue_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{sub_issue_number}"
    issue_res = requests.get(issue_url, headers=headers)
    body = issue_res.json().get("body", "")
    match = re.search(r"Est:\s*(\d+)(h|m)", body, re.IGNORECASE)
    if match:
        value = int(match.group(1))
        unit = match.group(2).lower()
        total_minutes += value * 60 if unit == "h" else value

hours = total_minutes // 60
minutes = total_minutes % 60
total_time = f"{hours}h {minutes}m"

# Gửi comment vào issue cha
comment_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{issue_number}/comments"
comment_body = {
    "body": f"⏱ Tổng thời gian ước lượng từ các sub-issues: **{total_time}**"
}
requests.post(comment_url, headers=headers, json=comment_body)

print(f"Tổng thời gian: {total_time}")