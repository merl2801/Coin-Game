import re
import os
from github import Github

def sum_time_spent(github_token, repo_name, parent_issue_id):
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    total_time = 0.0
    for issue in repo.get_issues(state="all", labels=["log", "work-time"]):
        body = issue.body or ""
        match_issue_id = re.search(r'issue_id[\s\S]*?(\d+)', body, re.IGNORECASE)
        if match_issue_id and int(match_issue_id.group(1)) == parent_issue_id:
            match_time = re.search(r'time_spent[\s\S]*?(\d+(?:\.\d+)?)', body, re.IGNORECASE)
            if match_time:
                total_time += float(match_time.group(1))
    return total_time

def comment_total_time(github_token, repo_name, parent_issue_id, total_time):
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    parent_issue = repo.get_issue(number=parent_issue_id)
    parent_issue.create_comment(f"Tổng thời gian từ các sub-issue: {total_time} giờ.")

if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("REPO_NAME")
    parent_issue_id = int(os.getenv("PARENT_ISSUE_ID", "0"))
    if not github_token or not repo_name or not parent_issue_id:
        print("Missing environment variables: GITHUB_TOKEN, REPO_NAME, PARENT_ISSUE_ID")
        exit(1)
    total_time = sum_time_spent(github_token, repo_name, parent_issue_id)
    print(f"Tổng thời gian từ các sub-issue: {total_time} giờ.")
    comment_total_time(github_token, repo_name, parent_issue_id, total_time)
