import requests


class OllamaService:
    def chat(self, prompt: str):
        print("CALLING OLLAMA")
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "mistral", "prompt": prompt, "stream": False},
                timeout=600,
            )

            response.raise_for_status()

            return response.json()["response"]

        except requests.Timeout:
            return "AI service timeout."
