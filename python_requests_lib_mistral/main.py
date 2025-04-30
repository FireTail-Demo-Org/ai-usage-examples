import requests

# Source: https://docs.mistral.ai/api/#tag/chat/operation/chat_completion_v1_chat_completions_post

API_URL = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "Who is the best French painter? Answer in one short sentence."}],
    "model": "command-a-03-2025",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
