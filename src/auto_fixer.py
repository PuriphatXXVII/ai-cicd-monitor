import anthropic
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
GH_TOKEN = os.getenv("GH_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")

headers = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_fix_suggestion(error_log: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "You are a DevOps expert. Given this CI/CD error, suggest a specific fix as a short code snippet or command only. No explanation needed.\n\nError:\n" + error_log
            }
        ]
    )
    return message.content[0].text

def get_main_sha() -> str:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/git/ref/heads/main"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["object"]["sha"]
    print(f"❌ Cannot get main SHA: {response.status_code} {response.text}")
    return ""

def create_fix_branch(branch_name: str, sha: str) -> bool:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/git/refs"
    data = {"ref": f"refs/heads/{branch_name}", "sha": sha}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"✅ Branch '{branch_name}' created!")
        return True
    print(f"❌ Failed to create branch: {response.status_code} {response.text}")
    return False

def create_fix_file(branch_name: str, fix_suggestion: str) -> bool:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/fixes/fix-suggestion.md"
    content = f"# Auto-Fix Suggestion\n\n```\n{fix_suggestion}\n```"
    data = {
        "message": "🤖 auto-fix: add fix suggestion",
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch_name
    }
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"✅ Fix file created!")
        return True
    print(f"❌ Failed to create file: {response.status_code} {response.text}")
    return False

def create_pull_request(branch_name: str, fix_suggestion: str, job_name: str) -> str:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls"
    data = {
        "title": f"🤖 Auto-fix: {job_name} pipeline failure",
        "body": f"## AI-Generated Fix\n\nThis PR was automatically created by AI-CICD-Monitor.\n\n### Suggested Fix:\n```\n{fix_suggestion}\n```\n\n> ⚠️ Please review before merging.",
        "head": branch_name,
        "base": "main"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        pr_url = response.json()["html_url"]
        print(f"✅ PR created: {pr_url}")
        return pr_url
    print(f"❌ Failed to create PR: {response.status_code} {response.text}")
    return ""

def auto_fix(job_name: str, error_log: str) -> str:
    print("🤖 Generating fix suggestion with Claude AI...")
    fix = get_fix_suggestion(error_log)
    
    sha = get_main_sha()
    if not sha:
        return ""
    
    import time
    branch_name = f"auto-fix/{job_name.lower().replace(' ', '-')}-{int(time.time())}"
    
    print(f"🌿 Creating branch: {branch_name}")
    if create_fix_branch(branch_name, sha):
        if create_fix_file(branch_name, fix):
            pr_url = create_pull_request(branch_name, fix, job_name)
            return pr_url
    return ""

if __name__ == "__main__":
    test_error = "Error: npm install failed - ENOENT: no such file or directory, open 'package.json'"
    auto_fix("Build and Test", test_error)