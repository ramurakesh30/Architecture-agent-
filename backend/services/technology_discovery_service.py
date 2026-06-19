import json

from backend.services.ollama_service import OllamaService


class TechnologyDiscoveryService:
    def __init__(self):

        self.ollama = OllamaService()

    def discover(self, report: dict):

        prompt = f"""
You are an architecture discovery engine.

Analyze the following assessment report.

Extract all technologies that appear to be used.

Return ONLY valid JSON.

Example:

{{
  "cloud": ["AWS"],
  "compute": ["Kubernetes"],
  "storage": ["S3"],
  "database": ["PostgreSQL"],
  "networking": ["Ingress"],
  "iac": ["Terraform"],
  "security": ["IAM"]
}}

Assessment Report:

{report}
"""

        response = self.ollama.chat(prompt)

        try:
            return json.loads(response)

        except Exception:
            return {
                "cloud": [],
                "compute": [],
                "storage": [],
                "database": [],
                "networking": [],
                "iac": [],
                "security": [],
            }
