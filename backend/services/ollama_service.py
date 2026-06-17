import requests


class OllamaService:

    def chat(
        self,
        prompt: str
    ):
        print(
            "CALLING OLLAMA"
        )

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model":
                "mistral",

                "prompt":
                prompt,

                "stream":
                False

            }

        )

        response.raise_for_status()

        return response.json()[
            "response"
        ]