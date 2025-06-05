import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-r-plus-08-2024",
    messages=[cohere.UserChatMessageV2(content="hello world!")],
    temperature=0.5,
)

print(response)
