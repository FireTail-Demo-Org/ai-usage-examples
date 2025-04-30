import requests

# Source: https://github.com/AI21Labs/ai21-python?tab=readme-ov-file & https://docs.ai21.com/reference/jamba-1-6-api-ref

API_URL = "https://api.ai21.com/v1/chat/completions"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "Hello, I need help with a signup process."}],
    "model": "jamba-mini",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
