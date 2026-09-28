# AI Engineer — Learning Log

Hands-on lessons covering core LLM engineering concepts, from basic API calls to structured output with Pydantic.

## Topics

| #  | Topic                        | Folder                                                      | Key File             |
| -- | ---------------------------- | ----------------------------------------------------------- | -------------------- |
| 01 | First LLM API Call           | [01-llm-call](./01-llm-call/)                               | `llm.py`             |
| 02 | System Role & Temperature    | [02-system-role-temperature](./02-system-role-temperature/)  | `sys_temp.py`        |
| 03 | Tokens & Usage               | [03-tokens](./03-tokens/)                                   | `tokens.py`          |
| 04 | Pydantic + JSON Mode         | [04-pydantic-json](./04-pydantic-json/)                     | `json_pydantic.py`   |

## Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd ai-engineer

# 2. Create a .env file in the project root with your API key
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Install dependencies
uv sync --all-packages

# 4. Run any lesson
cd 03-tokens
uv run python tokens.py
```

> **Note:** You need a [Groq](https://console.groq.com/) API key. Never commit your `.env` file — it is already in `.gitignore`.

## About

This repository is a personal learning log for the **AI Engineer** track. Each folder is a self-contained lesson with its own script, README, and dependencies managed by [uv](https://docs.astral.sh/uv/) workspaces.
