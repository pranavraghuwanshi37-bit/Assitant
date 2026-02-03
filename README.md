# Clawdbot-Plus Assistant

A starter scaffold for building an AI assistant that aims to surpass "clawdbot" with:

- **Modular brain** (LLM adapter + tools + memory).
- **Safety-first design** (policy checks and guardrails).
- **Extensible skills** (drop-in tools and workflows).

## Goals

- Build a fast, reliable assistant with a clean API.
- Support multiple LLM providers via adapters.
- Add tool execution, memory, and retrieval.
- Provide a testable, production-ready structure.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m assistant
```

## Architecture

```
assistant/
  app.py        # CLI entry + orchestration
  brain.py      # Decision loop + tool routing
  config.py     # Settings + environment handling
  memory.py     # Simple memory store (swap for vector DB)
  tools.py      # Tool registry and implementations
```

## Next steps

1. Swap in your preferred LLM provider in `brain.py`.
2. Add tools in `tools.py` for APIs, databases, and file ops.
3. Replace `memory.py` with a vector database for long-term memory.
4. Add an HTTP API (FastAPI) if you want a web client.

## Notes

- This is a minimal foundation. Expand modules as you add capabilities.
- Use `.env` for secrets (see `.env.example`).
