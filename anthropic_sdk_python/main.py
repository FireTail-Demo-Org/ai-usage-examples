import anthropic
from anthropic.types import MessageParam

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

messages: list[MessageParam] = [
    {
        "role": "user",
        "content": "Hello, Claude",
    },
]

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=messages,
)

print(message.content)
