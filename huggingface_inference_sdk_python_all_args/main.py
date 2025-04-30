from huggingface_hub import (
    ChatCompletionInputFunctionDefinition,
    ChatCompletionInputGrammarType,
    ChatCompletionInputStreamOptions,
    ChatCompletionInputTool,
    InferenceClient,
)

messages = [
    {
        "role": "user",
        "content": "What is the capital of France?",
    }
]

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    provider="together",
    token="PLACEHOLDER_TOKEN",
    timeout=3.14159,
    headers={
        "PLACEHOLDER-HEADER": "PLACEHOLDER-VALUE",
    },
    cookies={
        "PLACEHOLDER-COOKIE": "PLACEHOLDER-VALUE",
    },
    proxies="PLACEHOLDER_PROXY_VALUE",
    bill_to="PLACEHOLDER_BILL_TO",
    base_url="PLACEHOLDER_BASE_URI",
    api_key="PLACEHOLDER_API_KEY",
)

response = client.chat_completion(
    messages,
    model="",
    stream=False,
    frequency_penalty=3.14159,
    logit_bias=[0, 1, 2, 3],
    logprobs=False,
    max_tokens=100,
    n=1,
    presence_penalty=3.14159,
    response_format=ChatCompletionInputGrammarType(type="text"),
    seed=12093847,
    stop=["PLACEHOLDER_STOP"],
    stream_options=ChatCompletionInputStreamOptions(include_usage=False),
    temperature=0.7,
    tool_choice="auto",
    tool_prompt="PLACEHOLDER_TOOL_PROMPT",
    tools=[
        ChatCompletionInputTool(
            function=ChatCompletionInputFunctionDefinition(
                arguments={"PLACEHOLDER_ARGUMENTS_KEY": "PLACEHOLDER_ARGUMENTS_VALUE"},
                name="PLACEHOLDER_NAME",
                description="PLACEHOLDER_DESCRIPTION",
            ),
            type="PLACEHOLDER_TYPE",
        )
    ],
    top_p=3.14159,
    extra_body={
        "PLACEHOLDER_EXTRA_BODY_KEY": "PLACEHOLDER_EXTRA_BODY_VALUE",
    },
)

print(response.choices[0].message.content)
