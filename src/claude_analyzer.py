import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_error(log_text):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "You are a DevOps expert. Analyze this CI/CD pipeline error log and provide: 1. What went wrong 2. Root cause 3. How to fix it\n\nError log:\n" + log_text
            }
        ]
    )
    return message.content[0].text

if __name__ == "__main__":
    test_log = "Error: npm install failed - ENOENT: no such file or directory, open 'package.json'"
    result = analyze_error(test_log)
    print(result)