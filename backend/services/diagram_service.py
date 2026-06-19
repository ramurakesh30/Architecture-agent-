import json

from backend.services.ollama_service import OllamaService


class DiagramService:
    def __init__(self):

        self.ollama = OllamaService()

    def generate_diagram(self, report: dict):

        prompt = f"""
You are an architecture discovery engine.

Assessment Report:

{json.dumps(report, indent=2)}

Generate a Mermaid diagram representing
the CURRENT architecture.

Rules:

1. Only use components found in the report.
2. Do NOT redesign.
3. Do NOT improve architecture.
4. Do NOT add components not present.
5. Do NOT add WAF, ALB, Secrets Manager,
   RDS, CloudWatch, etc unless explicitly present.

Return ONLY Mermaid.

Start with:

graph TD
"""

        diagram = self.ollama.chat(prompt)

        diagram = diagram.replace("```mermaid", "").replace("```", "").strip()

        if not diagram.startswith("graph"):
            diagram = """
graph TD

Repository --> Analysis
Analysis --> Findings
"""

        return {"diagram": diagram}
