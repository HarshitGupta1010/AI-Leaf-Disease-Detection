import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    groq_api_key: str
    model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"
    model_temperature: float = 0.3
    max_completion_tokens: int = 1024

    @classmethod
    def from_env(cls) -> 'AppConfig':
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")

        return cls(
            groq_api_key=groq_api_key,
            model_name=os.getenv("MODEL_NAME", cls.model_name),
            model_temperature=float(
                os.getenv("MODEL_TEMPERATURE", cls.model_temperature)),
            max_completion_tokens=int(
                os.getenv("MAX_COMPLETION_TOKENS", cls.max_completion_tokens)),
        )
