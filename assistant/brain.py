"""Core orchestration logic for the assistant."""
from dataclasses import dataclass
from typing import List

from .config import Settings
from .memory import Memory
from .tools import ToolRegistry


@dataclass
class Response:
    text: str
    used_tools: List[str]


class Brain:
    """Basic decision loop for routing and response synthesis."""

    def __init__(self, settings: Settings, memory: Memory, tools: ToolRegistry) -> None:
        self.settings = settings
        self.memory = memory
        self.tools = tools

    def handle(self, user_input: str) -> Response:
        self.memory.add(f"User: {user_input}")

        if user_input.lower().startswith("use tool:"):
            _, _, rest = user_input.partition(":")
            tool_name, _, payload = rest.strip().partition(" ")
            tool_result = self.tools.run(tool_name, payload)
            response_text = f"Tool result: {tool_result}"
            self.memory.add(f"Assistant: {response_text}")
            return Response(text=response_text, used_tools=[tool_name])

        response_text = (
            f"{self.settings.assistant_name} (" f"{self.settings.model_name}) heard: {user_input}"
        )
        self.memory.add(f"Assistant: {response_text}")
        return Response(text=response_text, used_tools=[])
