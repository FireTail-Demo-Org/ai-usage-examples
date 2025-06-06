import os

from mistralai import (
    AssistantMessage,
    Messages,
    MessagesTypedDict,
    Mistral,
    RetryConfig,
    SystemMessage,
    ToolMessage,
    UserMessage,
)
from mistralai.utils import BackoffStrategy

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(
    api_key=api_key,
    server="https://api.mistral.ai",
    server_url="https://api.mistral.ai/v1",
    url_params={"model": model},
    client=None,  # You can pass an httpx.Client instance if needed
    async_client=None,  # You can pass an httpx.AsyncClient instance if needed
    retry_config=None,  # Use default retry configuration
    timeout_ms=60000,  # Set timeout to 60 seconds
    debug_logger=None,  # Use default logger
)

messages: list[MessagesTypedDict | Messages] = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provides information about cheeses.",
    },
    {
        "role": "user",
        "content": "What is the best French cheese?",
    },
    {
        "role": "assistant",
        "content": "The best French cheese is subjective, but many people consider Roquefort to be one of the finest. It is a blue cheese made from sheep's milk and has a strong, tangy flavor.",
        "tool_calls": [],
        "prefix": False,
    },
    {
        "role": "tool",
        "content": "tool",
        "tool_call_id": "tool-call-id-123",
        "name": "cheese_info_tool",
    },
    AssistantMessage(
        content="What is the best cheese in Italy?",
        role="assistant",
        tool_calls=[],
        prefix=False,
    ),
    SystemMessage(
        content="You are a helpful assistant that provides information about cheeses.",
        role="system",
    ),
    ToolMessage(
        content="tool",
        tool_call_id="tool-call-id-456",
        name="cheese_info_tool",
    ),
    UserMessage(
        content="What is the best cheese in Italy?",
        role="user",
    ),
]

chat_response = client.chat.complete(
    messages=messages,  # type: ignore
    model=model,
    max_tokens=100,
    temperature=0.7,
    top_p=1.0,
    stream=False,
    stop=["\n"],
    random_seed=42,
    tools=[],  # No tools used in this example
    response_format=None,  # Use default response format
    tool_choice=None,  # No tool choice in this example
    presence_penalty=0.0,
    frequency_penalty=0.0,
    n=1,  # Number of completions to generate
    prediction=None,  # No specific prediction in this example
    parallel_tool_calls=False,  # No parallel tool calls in this example
    safe_prompt=None,  # No safe prompt in this example
    retries=RetryConfig(
        strategy="exponential",  # Retry strategy
        backoff=BackoffStrategy(
            initial_interval=1000,  # Initial backoff interval in milliseconds
            max_interval=30000,  # Maximum backoff interval in milliseconds
            exponent=2.0,  # Exponential backoff factor
            max_elapsed_time=60000,  # Maximum elapsed time for retries in milliseconds
        ),
        retry_connection_errors=False,  # Do not retry on connection errors
    ),  # No retries in this example
    server_url="https://api.mistral.ai/v1",
    timeout_ms=60000,  # Set timeout to 60 seconds
    http_headers={"Custom-Header": "value"},  # Custom headers if needed
)

print(chat_response.choices[0].message.content)
