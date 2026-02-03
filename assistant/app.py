"""CLI entrypoint for the assistant."""
from .brain import Brain
from .config import load_settings
from .memory import Memory
from .tools import build_default_registry


def run() -> None:
    settings = load_settings()
    memory = Memory()
    tools = build_default_registry()
    brain = Brain(settings=settings, memory=memory, tools=tools)

    print(f"{settings.assistant_name} is ready. Type 'quit' to exit.")

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        response = brain.handle(user_input)
        print(response.text)


if __name__ == "__main__":
    run()
