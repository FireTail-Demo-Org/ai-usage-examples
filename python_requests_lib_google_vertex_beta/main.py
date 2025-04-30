import requests

# Source: https://ai.google.dev/gemini-api/docs/openai#rest

API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "Explain to me how AI works"}],
    "model": "gemini-2.0-flash",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
