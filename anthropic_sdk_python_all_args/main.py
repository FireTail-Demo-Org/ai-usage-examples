from anthropic import Anthropic
from anthropic.types import MessageParam, MetadataParam, ToolChoiceAutoParam, ToolParam

client = Anthropic(
    api_key="my_api_key",
    auth_token="my_auth_token",
    base_url="https://api.anthropic.com",
    timeout=3.14159,
    max_retries=5,
    default_headers={
        "PLACEHOLDER-HEADER": "PLACEHOLDER-VALUE",
    },
    default_query={
        "PLACEHOLDER_QUERY": "PLACEHOLDER-VALUE",
    },
    http_client=None,
    transport=None,
    proxies=None,
    connection_pool_limits=None,
    _strict_response_validation=True,
)

messages: list[MessageParam] = [
    {
        "role": "user",
        "content": "Hello, Claude",
    },
]

message = client.messages.create(
    max_tokens=1024,
    messages=messages,
    model="claude-3-7-sonnet-20250219",
    metadata=MetadataParam(user_id="user_id"),
    stop_sequences=["PLACEHOLDER_STOP"],
    stream=False,
    system="PLACEHOLDER_SYSTEM",
    temperature=0.7,
    tool_choice=ToolChoiceAutoParam(type="auto", disable_parallel_tool_use=False),  # type: ignore
    tools=[
        ToolParam(
            name="PLACEHOLDER_NAME",
            description="PLACEHOLDER_DESCRIPTION",
            input_schema={
                "type": "object",
                "properties": {},
            },
        )
    ],
    top_k=3,
    top_p=3.14159,
    extra_headers={
        "PLACEHOLDER_HEADER": "PLACEHOLDER_VALUE",
    },
    extra_query={
        "PLACEHOLDER_QUERY": "PLACEHOLDER_VALUE",
    },
    extra_body={
        "PLACEHOLDER_BODY": "PLACEHOLDER_VALUE",
    },
    timeout=3.14159,
)

print(message.content)
