import os
import requests
import re
import json

REPO = os.getenv('GITHUB_REPOSITORY')
TOKEN = os.getenv('GITHUB_TOKEN')
API_URL = f"https://api.github.com/repos/{REPO}"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_issue(event_path):
    with open(event_path, 'r', encoding='utf-8') as f:
        event = json.load(f)
    return event['issue']['number']

def get_all_issues():
    # Lấy tất cả các issue có label 'log' và 'work-time'
    issues = []
    page = 1
    while True:
        r = requests.get(f"{API_URL}/issues", headers=headers, params={"state": "all", "labels": "log,work-time", "per_page": 100, "page": page})
        data = r.json()
        if not data:
            break
        issues.extend(data)
        page += 1
    return issues

def extract_time_spent(issue):
    match = re.search(r'time_spent.*?(\d+(\.\d+)?)', issue.get('body', ''))
    if match:
        return float(match.group(1))
    return 0.0

def update_parent_issue(parent_issue_number, total_time):
    comment = f"⏱ Tổng thời gian các sub-issue: **{total_time} giờ**"
    requests.post(f"{API_URL}/issues/{parent_issue_number}/comments", headers=headers, json={"body": comment})

if __name__ == "__main__":
    event_path = os.getenv('GITHUB_EVENT_PATH')
    issue_number = get_issue(event_path)
    all_issues = get_all_issues()
    total_time = sum(extract_time_spent(issue) for issue in all_issues)
    update_parent_issue(issue_number, total_time)
