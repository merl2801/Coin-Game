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

def get_sub_issues(parent_issue_number):
    # Lấy các issue có trường 'issue_id' là số của issue cha
    r = requests.get(f"{API_URL}/issues", headers=headers, params={"state": "open", "labels": "log,work-time"})
    sub_issues = []
    for issue in r.json():
        body = issue.get('body', '')
        match = re.search(r'issue_id.*?(\d+)', body)
        if match and match.group(1) == str(parent_issue_number):
            sub_issues.append(issue)
    return sub_issues

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
    parent_issue_number = get_issue(event_path)
    sub_issues = get_sub_issues(parent_issue_number)
    total_time = sum(extract_time_spent(issue) for issue in sub_issues)
    update_parent_issue(parent_issue_number, total_time)
