from huggingface_hub import InferenceClient

messages = [
    {
        "role": "user",
        "content": "What is the capital of France?",
    }
]

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    provider="together",
)

response = client.chat_completion(
    messages,
    max_tokens=100,
    temperature=0.7,
)

print(response.choices[0].message.content)
