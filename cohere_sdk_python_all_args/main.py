from concurrent.futures import ThreadPoolExecutor

import cohere

co = cohere.ClientV2(
    api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    base_url="https://api.cohere.com/v2/chat",
    environment=cohere.ClientEnvironment.PRODUCTION,
    client_name="cohere-python-sdk",
    timeout=3.14159,
    httpx_client=None,
    thread_pool_executor=ThreadPoolExecutor(64),
    log_warning_experimental_features=True,
)

response = co.chat(
    model="command-r-plus-08-2024",
    messages=[
        cohere.UserChatMessageV2(content="hello world!"),
        cohere.AssistantChatMessageV2(tool_calls=None, tool_plan=None, content="assistant message", citations=None),
        cohere.SystemChatMessageV2(content="system message"),
        cohere.ToolChatMessageV2(tool_call_id="tool_call_id", content="tool message"),
    ],
    tools=[],
    strict_tools=False,
    documents=[],
    citation_options=cohere.CitationOptions(mode="FAST"),
    response_format=cohere.JsonObjectResponseFormatV2(),
    safety_mode="none",
    max_tokens=100,
    stop_sequences=[],
    temperature=0.5,
    seed=42,
    frequency_penalty=0,
    presence_penalty=0,
    k=0,
    p=0,
    return_prompt=False,
    logprobs=True,
    tool_choice="auto",
    request_options=None,
)

print(response)
