from ai21 import AI21Client, AI21EnvConfig
from ai21.models.chat.chat_message import AssistantMessage, ChatMessage, SystemMessage, ToolMessage, UserMessage
from ai21.models.chat.response_format import ResponseFormat

system = "You're a support engineer in a SaaS company"
messages = [
    SystemMessage(content=system, role="system"),
    UserMessage(content="Hello, I need help with a signup process.", role="user"),
    AssistantMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    UserMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
    ChatMessage(
        content="I understand. Can you please provide me with the email address you used to sign up?",
        role="assistant",
    ),
    ToolMessage(
        content="tool",
        tool_call_id="tool-call-id-123",
    ),
]

client = AI21Client(
    api_key="your_api_key",
    api_host="https://api.ai21.com",
    headers={"Custom-Header": "value"},
    timeout_sec=60,
    num_retries=5,
    via="https://via.example.com",
    http_client=None,  # You can pass an httpx.Client instance if needed
    env_config=AI21EnvConfig,  # Use default AI21 environment configuration
)

response = client.chat.completions.create(
    model="jamba-mini",
    messages=messages,
    max_tokens=100,
    temperature=0.7,
    top_p=1.0,
    stop=["\n"],
    n=1,
    stream=False,
    tools=[],
    response_format=ResponseFormat(type="text"),
    documents=[],
)
