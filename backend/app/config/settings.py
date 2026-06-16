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

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )
    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

    SUPPORTED_EXTENSIONS = {

        ".py",
        ".yaml",
        ".yml",
        ".json",
        ".tf",
        ".tfvars",
        ".sh",
        ".js",
        ".ts",
        ".tsx",
        ".jsx",
        ".java",
        ".go",
        ".sql",
        ".md",
        ".dockerfile"
    }
