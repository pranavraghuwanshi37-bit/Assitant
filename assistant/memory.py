"""Memory subsystem for the assistant."""
from dataclasses import dataclass, field
from typing import Deque, List
from collections import deque


@dataclass
class Memory:
    """Simple rolling memory buffer."""

    max_items: int = 20
    _items: Deque[str] = field(default_factory=deque, init=False)

    def add(self, entry: str) -> None:
        self._items.append(entry)
        while len(self._items) > self.max_items:
            self._items.popleft()

    def snapshot(self) -> List[str]:
        return list(self._items)
