import os
import re
import requests

body = os.environ["ISSUE_BODY"]
issue_number = os.environ["ISSUE_NUMBER"]
repo = os.environ["REPO"]
token = os.environ["GITHUB_TOKEN"]

# Tìm các số trong issue (template đã chuẩn hóa nên chỉ cần lấy các số)
numbers = re.findall(r"\b\d+\b", body)
numbers = list(map(int, numbers))

if numbers:
    result = sum(numbers)
    comment_body = f"✅ Kết quả tự động: Tổng các số bạn nhập là **{result}**."
else:
    comment_body = "⚠️ Không tìm thấy số hợp lệ để tính toán."

# Comment lại vào issue
url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json",
}
data = {"body": comment_body}

resp = requests.post(url, headers=headers, json=data)
resp.raise_for_status()

print(f"Đã comment: {comment_body}")
