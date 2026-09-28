# 04 — Structured Output with Pydantic & JSON Mode

## Why Structured Output?

By default an LLM returns free-form text. That's great for chat, but when you need to feed the result into another program — a database, an API, a dashboard — you need **predictable, machine-readable output**.

Two tools solve this:

| Tool             | Role                                                                 |
| ---------------- | -------------------------------------------------------------------- |
| **JSON mode**    | Tells the LLM to respond with valid JSON (`response_format={"type": "json_object"}`). |
| **Pydantic**     | Defines a Python schema and validates the JSON against it at runtime. |

## Key Concepts

### Pydantic `BaseModel`

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

- Declares the **fields** and **types** you expect.
- `Ticket.model_json_schema()` gives a JSON Schema you can include in the prompt so the LLM knows what shape to produce.
- `Ticket(**data)` validates and converts raw dict → typed Python object.

### JSON Mode

```python
response_format = {"type": "json_object"}
```

Pass this to `client.chat.completions.create(...)`. The model is now **guaranteed** to return valid JSON (no markdown fences, no extra prose).

### The Flow

```
User text  ─→  LLM (with schema in system prompt + JSON mode)  ─→  JSON string
                                                                       │
                                                              json.loads()
                                                                       │
                                                              Pydantic validates
                                                                       │
                                                              Typed Python object
```

## What `json_pydantic.py` Does

1. Defines a `Ticket` schema with `name`, `email`, and `issue`.
2. Sends a mock customer-support message to the LLM with the schema in the system prompt.
3. Receives a JSON response, parses it with `json.loads`, and validates it with Pydantic.
4. Prints the structured fields individually.

## Run

```bash
cd 04-pydantic-json
uv run python json_pydantic.py
```

## Example Output

```json
{"name": "XYZ", "email": "abc@gmail.com", "issue": "iPhone is not working at all"}
```

```
XYZ
abc@gmail.com
iPhone is not working at all
```

## Takeaway

Combining **JSON mode** with **Pydantic** gives you the best of both worlds: the LLM produces valid JSON, and Pydantic enforces your schema at runtime — catching missing fields or wrong types before they reach the rest of your code.
