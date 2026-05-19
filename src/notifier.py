import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_notification(job_name: str, status: str, analysis: str):
    if status == "failure":
        color = 15158332  # แดง
        emoji = "🔴"
    else:
        color = 3066993   # เขียว
        emoji = "🟢"

    embed = {
        "embeds": [
            {
                "title": f"{emoji} CI/CD Pipeline Alert: {job_name}",
                "description": analysis[:2000],
                "color": color,
                "footer": {"text": "AI-CICD-Monitor | Powered by Claude AI"}
            }
        ]
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=embed)
    if response.status_code == 204:
        print("✅ Discord notification sent!")
    else:
        print(f"❌ Failed: {response.status_code}")

if __name__ == "__main__":
    send_discord_notification(
        job_name="Test Pipeline",
        status="failure",
        analysis="Test message from AI-CICD-Monitor!"
    )