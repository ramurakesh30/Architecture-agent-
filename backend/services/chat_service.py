import json

from backend.services.ollama_service import (
    OllamaService
)


class ChatService:

    def __init__(self):

        self.ollama = (
            OllamaService()
        )

    def answer_question(

        self,

        report: dict,

        question: str

    ):
        print(
            "QUESTION:",
            question
        )

        context = json.dumps(

            report,

            indent=2

        )

        prompt = f"""
You are an enterprise architecture reviewer.

You specialize in:

- AWS
- Azure
- Kubernetes
- Terraform
- Security
- Infrastructure

Assessment Report:

{context}

Question:

{question}

Requirements:

1. Explain findings clearly.
2. Prioritize risks.
3. Suggest remediation.
4. Be specific.
5. Do not invent information.
"""

        answer = (

            self.ollama.chat(
                prompt
            )

        )

        return {

            "answer":
            answer

        }