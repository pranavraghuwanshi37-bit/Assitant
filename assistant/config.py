"""Configuration utilities for the assistant."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Runtime configuration values."""

    assistant_name: str
    llm_provider: str
    model_name: str


def load_settings() -> Settings:
    """Load configuration from environment variables with sensible defaults."""
    return Settings(
        assistant_name=os.getenv("ASSISTANT_NAME", "Clawdbot-Plus"),
        llm_provider=os.getenv("LLM_PROVIDER", "mock"),
        model_name=os.getenv("MODEL_NAME", "mock-model"),
    )
