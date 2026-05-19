# 🤖 AI-Powered CI/CD Pipeline Monitor

> Automatically detects pipeline failures, analyzes errors with Claude AI, and sends instant Discord notifications.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Claude AI](https://img.shields.io/badge/Claude-AI-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-green)
![Discord](https://img.shields.io/badge/Discord-Webhook-purple)

---

## 🚀 Features

- **AI Error Analysis** — Uses Claude AI to analyze CI/CD pipeline errors and suggest fixes
- **Instant Discord Alerts** — Sends formatted notifications to Discord when pipeline fails
- **GitHub Actions Integration** — Automatically triggers on every push and pull request
- **Actionable Insights** — Provides root cause analysis and step-by-step fix instructions

---

## 🏗️ Architecture
GitHub Actions (pipeline fails)
↓
monitor.py (detects failure)
↓
claude_analyzer.py (Claude AI analyzes error)
↓
notifier.py (sends Discord notification)
↓
Discord Channel #ai-cicd-monitor

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Claude API (Anthropic) | AI error analysis |
| Discord Webhook | Notifications |
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
│   └── notifier.py
├── .env.example
├── requirements.txt
└── README.md

---

## 👤 Author

**Puriphat Srikamnoi**  
[GitHub](https://github.com/PuriphatXXVII)