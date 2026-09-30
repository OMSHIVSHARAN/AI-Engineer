# LLM Learning Log

**Date:** September 30, 2026  
**Topic:** LLM Fundamentals and API Integration

## 1. What are LLMs?
Large Language Models (LLMs) are AI models trained on large amounts of text to understand and generate human language. Examples include GPT, Claude, and Llama.

## 2. How Do LLMs Work?
Most modern LLMs use the Transformer architecture. They process input text as tokens and predict the next token to generate responses.

## 3. Tokens and Tokenization
Tokens are small units of text processed by LLMs. Tokenization converts text into tokens that the model can understand. API costs and context limits often depend on token usage.

## 4. System, User, and Assistant Messages
- **System:** Defines the model's behavior.
- **User:** Contains the input or question.
- **Assistant:** Contains the model's response.

## 5. Prompt Engineering
Prompt engineering is the process of designing effective instructions to get useful and accurate responses from LLMs.

Common techniques include clear instructions, providing context, and few-shot prompting.

## 6. Temperature
Temperature controls the randomness of an LLM's responses.

- **Low temperature:** More consistent and predictable outputs.
- **High temperature:** More varied and creative outputs.

## 7. Calling an LLM API Using Python and Groq
The Groq API allows developers to access LLMs using Python.

```python
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "What is an LLM?"}
    ],
    temperature=0.3
)

print(response.choices[0].message.content)
```
