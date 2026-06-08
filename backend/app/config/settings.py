import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    AI_PROVIDER = os.getenv(
        "AI_PROVIDER",
        "ollama"
    )

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:3b"
    )
