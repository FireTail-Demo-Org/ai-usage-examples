import requests

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
payload = {
    "messages": [{"role": "user", "content": "How many 'G's in 'huggingface'?"}],
    "model": "deepseek/deepseek-v3-0324",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
