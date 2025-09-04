import os
import requests

token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("REPO")
issue_number = os.getenv("ISSUE_NUMBER")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

owner, repo_name = repo.split("/")
base_url = f"https://api.github.com/repos/{owner}/{repo_name}"

# 1. Lấy issue hiện tại
issue_url = f"{base_url}/issues/{issue_number}"
res = requests.get(issue_url, headers=headers)
res.raise_for_status()
issue_data = res.json()

# 2. Lấy ID của issue cha từ field `issue_id` (ghi trong template)
parent_id = None
body_text = issue_data.get("body", "")

for line in body_text.splitlines():
    if line.lower().startswith("issue:") or line.lower().startswith("issue_id:"):
        # Ví dụ: "Issue: 123"
        try:
            parent_id = int(line.split(":")[1].strip())
        except:
            pass
        break

if not parent_id:
    print("ℹ️ Không tìm thấy issue cha (issue_id) → không cần sum.")
    exit(0)

print(f"📌 Sub-issue #{issue_number} thuộc về issue cha #{parent_id}")

# 3. Tìm tất cả issue có chứa "Issue: <parent_id>" trong body (tức sub-issues)
query = f"repo:{repo} in:body 'Issue: {parent_id}'"
search_url = f"https://api.github.com/search/issues?q={query}"
search_res = requests.get(search_url, headers=headers)
search_res.raise_for_status()
items = search_res.json().get("items", [])

total_hours = 0.0

for item in items:
    body = item.get("body", "")
    for line in body.splitlines():
        if line.lower().startswith("作業時間") or "time_spent" in line.lower():
            # Ví dụ template ghi: "作業時間 (h) *: 2.5"
            parts = line.split(":")
            if len(parts) >= 2:
                try:
                    total_hours += float(parts[1].strip())
                except:
                    pass

# 4. Comment vào issue cha
comment_url = f"{base_url}/issues/{parent_id}/comments"
comment_body = {
    "body": f"⏱ Tổng thời gian cộng dồn từ các sub-issues: **{total_hours}h**"
}
post_res = requests.post(comment_url, headers=headers, json=comment_body)
if post_res.ok:
    print(f"✅ Đã cập nhật tổng thời gian {total_hours}h cho issue #{parent_id}")
else:
    print(f"⚠️ Lỗi khi gửi comment: {post_res.status_code} {post_res.text}")
