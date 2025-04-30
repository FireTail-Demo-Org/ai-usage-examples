import requests

# Source: https://docs.anthropic.com/en/api/messages

API_URL = "https://api.anthropic.com/v1/messages"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "Hello, world"}],
    "model": "claude-3-7-sonnet-20250219",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
