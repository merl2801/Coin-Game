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
    body = issue.get('body', '')
    # Tìm số sau dòng chứa '### 作業時間 (h) *'
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if '作業時間' in line:
            # Tìm dòng tiếp theo có số
            for j in range(i+1, len(lines)):
                match = re.search(r'(\d+(\.\d+)?)', lines[j])
                if match:
                    return float(match.group(1))
    return 0.0

def update_parent_issue(parent_issue_number, total_time):
    comment = f"🚀 [BOT] Đã tổng hợp xong! Tổng thời gian các sub-issue: **{total_time} giờ**"
    response = requests.post(f"{API_URL}/issues/{parent_issue_number}/comments", headers=headers, json={"body": comment})
    print(f"[DEBUG] Comment response: {response.status_code}, {response.text}")
def extract_issue_id(body):
    # Tìm số sau dòng chứa '### Issue'
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if 'Issue' in line:
            # Tìm dòng tiếp theo có số
            for j in range(i+1, len(lines)):
                match = re.search(r'(\d+)', lines[j])
                if match:
                    return match.group(1)
    return None

if __name__ == "__main__":
    event_path = os.getenv('GITHUB_EVENT_PATH')
    issue_number = get_issue(event_path)
    print(f"[DEBUG] Issue vừa tạo/cập nhật: {issue_number}")
    # Lấy nội dung issue vừa tạo/cập nhật
    with open(event_path, 'r', encoding='utf-8') as f:
        event = json.load(f)
    body = event['issue'].get('body', '')
    print(f"[DEBUG] Body: {body}")
    parent_issue_number = extract_issue_id(body)
    print(f"[DEBUG] Tìm thấy parent_issue_number: {parent_issue_number}")
    if parent_issue_number:
        # Tổng hợp tất cả sub-issue có issue_id trùng với parent_issue_number
        all_issues = get_all_issues()
        print(f"[DEBUG] Tổng số issue có label log,work-time: {len(all_issues)}")
        sub_issues = [issue for issue in all_issues if extract_issue_id(issue.get('body', '')) == parent_issue_number]
        print(f"[DEBUG] Số sub-issue liên quan: {len(sub_issues)}")
        total_time = sum(extract_time_spent(issue) for issue in sub_issues)
        print(f"[DEBUG] Tổng thời gian các sub-issue: {total_time}")
        update_parent_issue(parent_issue_number, total_time)
