import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer MY_API_KEY",
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [{"role": "user", "content": [{"type": "text", "text": "Hello, world"}]}],
    "audio": {"format": "mp3", "voice": "coral"},
    "frequency_penalty": 1,
    "function_call": "auto",
    "functions": [{"name": "function_name", "description": "Function description"}],
    "logit_bias": {"123": 1, "456": -1},
    "logprobs": True,
    "max_completion_tokens": 100,
    "max_tokens": 500,
    "metadata": {"key": "value"},
    "modalities": ["text", "image"],
    "n": 1,
    "parallel_tool_calls": True,
    "prediction": {"content": "predicted content", "type": "content"},
    "presence_penalty": 1.2,
    "reasoning_effort": "high",
    "response_format": {"type": "json_object"},
    "seed": 42,
    "service_tier": "auto",
    "stop": ["\n", "END"],
    "store": True,
    "stream": False,
    "stream_options": {"include_usage": True},
    "temperature": 0.7,
    "tool_choice": "auto",
    "tools": [{"function": {"name": "function_name", "description": "Function description"}, "type": "function"}],
    "top_logprobs": 5,
    "top_p": 0.9,
    "user": "user_id",
    "web_search_options": {
        "search_context_size": "high",
        "user_location": {
            "approximate": {"country": "IE"},
            "type": "approximate",
        },
    },
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()

print(response)
