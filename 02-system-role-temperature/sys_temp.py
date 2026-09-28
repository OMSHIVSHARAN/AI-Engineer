import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

role = "user"

content = "suggest a good name for a dog only 1 name"
message_system = {
    "role": "system",
    "content": "You are pet owner who suggests name."
}
message = {
    "role": role,
    "content": content
}

messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)

print(response.choices[0].message.content)