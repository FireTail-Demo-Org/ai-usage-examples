from google import genai
from google.genai import types
from PIL import Image

client = genai.Client(api_key="GEMINI_API_KEY")

# Here's a basic example that takes a single text input:

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"],
)
print(response.text)

# You can guide the behavior of Gemini models with system instructions. To do so, pass a GenerateContentConfig object.

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko.",
    ),
    contents="Hello there",
)

print(response.text)

# The GenerateContentConfig object also lets you override default generation parameters, such as temperature.

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1,
    ),
)
print(response.text)

# The Gemini API supports multimodal inputs, allowing you to combine text with media files. The following example
# demonstrates providing an image:

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "Tell me about this instrument"],
)
print(response.text)

# By default, the model returns a response only after the entire generation process is complete. For more fluid
# interactions, use streaming to receive GenerateContentResponse instances incrementally as they're generated.

streaming_response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"],
)
for chunk in streaming_response:
    print(chunk.text, end="")

# Our SDKs provide functionality to collect multiple rounds of prompts and responses into a chat, giving you an easy
# way to keep track of the conversation history.

chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f"role - {message.role}", end=": ")
    if message.parts is None:
        continue
    print(message.parts[0].text)


# Streaming can also be used for multi-turn conversations.

stream_response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in stream_response:
    print(chunk.text, end="")

stream_response = chat.send_message_stream("How many paws are in my house?")
for chunk in stream_response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f"role - {message.role}", end=": ")
    if message.parts is None:
        continue
    print(message.parts[0].text)
