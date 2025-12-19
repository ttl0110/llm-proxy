import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Lấy API Key từ biến môi trường để bảo mật
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Nhận dữ liệu thô từ curl
        prompt = request.data.decode('utf-8')
        
        if not prompt:
            return "Error: No prompt provided", 400

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "kwaipilot/kat-coder-pro:free", # Model miễn phí/rẻ và nhanh
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        
        result = response.json()['choices'][0]['message']['content']
        return result
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Render yêu cầu chạy trên port do họ cung cấp hoặc mặc định 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)