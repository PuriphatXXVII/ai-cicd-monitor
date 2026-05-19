# 🤖 AI-Powered CI/CD Pipeline Monitor

> Automatically detects pipeline failures, analyzes errors with Claude AI, creates fix suggestions, and opens Pull Requests automatically.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Claude AI](https://img.shields.io/badge/Claude-AI-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-green)
![Discord](https://img.shields.io/badge/Discord-Webhook-purple)

---

## 🚀 Features

- **AI Error Analysis** — Uses Claude AI to analyze CI/CD pipeline errors and suggest fixes
- **Auto-Fix PR** — Automatically creates a GitHub Pull Request with AI-generated fix
- **Instant Discord Alerts** — Sends formatted notifications to Discord when pipeline fails
- **GitHub Actions Integration** — Automatically triggers on every push and pull request

---

## 🏗️ Architecture
GitHub Actions (pipeline fails)
↓
monitor.py (detects failure)
↓
claude_analyzer.py (Claude AI analyzes error)
↓
auto_fixer.py (creates fix branch + PR automatically)
↓
notifier.py (sends Discord notification)
↓
Discord Channel #ai-cicd-monitor

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Claude API (Anthropic) | AI error analysis & fix suggestion |
| GitHub API | Auto branch & PR creation |
| Discord Webhook | Instant notifications |
| GitHub Actions | CI/CD automation |

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/PuriphatXXVII/ai-cicd-monitor.git
cd ai-cicd-monitor
```

### 2. Install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
```
Fill in your `.env` file:
ANTHROPIC_API_KEY=your_claude_api_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
GH_TOKEN=your_github_personal_access_token
GITHUB_REPO=your_username/ai-cicd-monitor

### 4. Run locally
```bash
python src/monitor.py
```

---

## 📦 Project Structure
ai-cicd-monitor/
├── .github/
│   └── workflows/
│       └── monitor.yml
├── src/
│   ├── monitor.py
│   ├── claude_analyzer.py
│   ├── auto_fixer.py
│   └── notifier.py
├── .env.example
├── requirements.txt
└── README.md

---

## 🔄 How It Works

1. GitHub Actions detects a pipeline failure
2. `monitor.py` captures the error log
3. `claude_analyzer.py` sends the log to Claude AI for analysis
4. `auto_fixer.py` creates a new branch and opens a PR with the fix
5. `notifier.py` sends an alert to Discord with full analysis

---

## 👤 Author

**Puriphat Srikamnoi**  
[GitHub](https://github.com/PuriphatXXVII)