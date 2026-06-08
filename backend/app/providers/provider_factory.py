from app.config.settings import (
    Settings
)

from app.providers.ollama_provider import (
    OllamaProvider
)

class ProviderFactory:

    @staticmethod
    def create():

        if (
            Settings.AI_PROVIDER
            == "ollama"
        ):

            return OllamaProvider(
                model=
                Settings.OLLAMA_MODEL
            )

        raise ValueError(
            f"Unsupported provider: "
            f"{Settings.AI_PROVIDER}"
        )