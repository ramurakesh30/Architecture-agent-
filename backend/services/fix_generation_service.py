import json

from backend.services.ollama_service import OllamaService


class FixGenerationService:
    def __init__(self):

        self.ollama = OllamaService()

    def generate_fix(self, report: dict, finding: str):

        context = json.dumps(report, indent=2)

        prompt = f"""
You are a senior cloud architect.

Assessment Report:

{context}

Finding:

{finding}

Tasks:

1. Explain the issue.
2. Explain the risk.
3. Recommend a fix.
4. Generate infrastructure code if applicable.
5. Return markdown.

Be concise and actionable.
"""

        response = self.ollama.chat(prompt)

        return {"fix": response}
