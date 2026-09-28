# 03 — Tokens & Usage

## What Are Tokens?

Tokens are the basic units that LLMs use to process text. A token can be a word, part of a word, or a punctuation mark. For example, the sentence `"Hello, world!"` might be split into `["Hello", ",", " world", "!"]` — four tokens.

Understanding tokens matters because:

- **You are billed per token** — both input (prompt) and output (completion).
- **Every model has a context window** — a maximum number of tokens it can handle in a single request.
- **Token limits control output length** — the `max_tokens` parameter caps how many tokens the model can generate.

## Key Concepts

| Concept              | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| **Prompt tokens**    | Number of tokens in the input (system + user messages).      |
| **Completion tokens**| Number of tokens the model generated in its response.        |
| **Total tokens**     | `prompt_tokens + completion_tokens`.                         |
| **max_tokens**       | Upper limit on completion length. If the response hits this, it is cut off. |
| **finish_reason**    | Why the model stopped: `"stop"` (natural end) or `"length"` (hit `max_tokens`). |

## What `tokens.py` Does

1. Sends three prompts of increasing complexity to the LLM — all capped at `max_tokens=50`.
2. Prints the token usage breakdown for each response.
3. Demonstrates how `finish_reason` changes from `"stop"` to `"length"` when a response is truncated.

## Run

```bash
cd 03-tokens
uv run python tokens.py
```

## Example Output

```
Prompt: Hi!
Prompt Tokens: 9
Completion Tokens: 12
Total Tokens: 21
Finish Reason: stop

Prompt: Explain time travel in detail in 100 words.
Prompt Tokens: 16
Completion Tokens: 50
Total Tokens: 66
Finish Reason: length
```

## Takeaway

Short prompts finish naturally (`stop`). When the answer needs more room than `max_tokens` allows, the model is forced to stop early (`length`). Monitoring token usage helps you control costs and avoid unexpected truncation.
