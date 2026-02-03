"""Tool registry and implementations."""
from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[[str], str]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def list_tools(self) -> List[Tool]:
        return list(self._tools.values())

    def run(self, name: str, payload: str) -> str:
        if name not in self._tools:
            return f"Tool '{name}' not found."
        return self._tools[name].handler(payload)


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()

    registry.register(
        Tool(
            name="echo",
            description="Echo back the provided text.",
            handler=lambda payload: f"Echo: {payload}",
        )
    )

    return registry
