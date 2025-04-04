import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer MY_API_KEY",
}

payload = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": [{"type": "text", "text": "Hello, world"}]}],
}

response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload).json()

print(response)
