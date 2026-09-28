import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=API_KEY)

MODEL = "openai/gpt-oss-120b"


def ask_llm(prompt, system_prompt="You are a helpful AI assistant."):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    return response.choices[0].message.content


# 1. Basic LLM call
print("=== BASIC ===")

response = ask_llm(
    "Explain what an LLM is in simple terms."
)

print(response)


# 2. System prompt
print("\n=== SYSTEM PROMPT ===")

response = ask_llm(
    "Explain recursion.",
    system_prompt="You are a programming teacher. Explain concepts using simple examples."
)

print(response)


# 3. Different task
print("\n=== CODE ===")

response = ask_llm(
    "Write a Python function that checks whether a number is prime."
)

print(response)