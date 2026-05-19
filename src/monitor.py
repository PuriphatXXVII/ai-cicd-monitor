import sys
import os
from claude_analyzer import analyze_error
from notifier import send_discord_notification

def monitor_pipeline(job_name: str, status: str, log_text: str):
    print(f"🔍 Monitoring pipeline: {job_name} - Status: {status}")
    
    if status == "failure":
        print("❌ Pipeline failed! Analyzing with Claude AI...")
        analysis = analyze_error(log_text)
        send_discord_notification(job_name, status, analysis)
        print("✅ Analysis sent to Discord!")
    else:
        send_discord_notification(job_name, status, "Pipeline completed successfully!")
        print("✅ Pipeline passed!")

if __name__ == "__main__":
    # ทดสอบ
    test_log = """
    Error: ENOENT: no such file or directory, open 'package.json'
    at Object.openSync (node:fs:601:3)
    npm ERR! code ENOENT
    npm ERR! syscall open
    npm ERR! path /github/workspace/package.json
    """
    
    monitor_pipeline(
        job_name="Build & Test",
        status="failure",
        log_text=test_log
    )