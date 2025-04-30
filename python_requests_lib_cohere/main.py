import requests

# Source: https://docs.cohere.com/reference/chat

API_URL = "https://api.cohere.com/v2/chat"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "Hello, world"}],
    "model": "command-a-03-2025",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
