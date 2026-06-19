import json

from backend.services.ollama_service import OllamaService
from backend.services.technology_discovery_service import TechnologyDiscoveryService


class RedesignService:
    def __init__(self):

        self.ollama = OllamaService()

        self.discovery = TechnologyDiscoveryService()

    def redesign(self, report: dict):

        technologies = self.discovery.discover(report)

        report_context = json.dumps(report, indent=2)

        technology_context = json.dumps(technologies, indent=2)

        prompt = f"""
You are a Principal Cloud Architect.

Analyze the current architecture assessment and
design a future-state target architecture.

Assessment Report:

{report_context}

Detected Technologies:

{technology_context}

Tasks:

1. Identify current weaknesses.
2. Design a production-ready target architecture.
3. Improve security.
4. Improve scalability.
5. Improve reliability.
6. Improve cost optimization.
7. Create a migration roadmap.
8. Generate a target architecture Mermaid diagram.

Target Architecture Requirements:

- Follow cloud best practices.
- Use least privilege security.
- Improve network isolation.
- Improve scalability.
- Improve observability.
- Improve operational excellence.

Diagram Requirements:

Include when appropriate:

- Internet
- WAF
- Load Balancer
- API Gateway
- Kubernetes Cluster
- Application Services
- Database
- Object Storage
- Secrets Manager
- Monitoring

Do NOT include:

- Pods
- Deployments
- Replica counts
- Security Groups
- Internal implementation details

Scorecard Requirements:

Use values from 0 to 10.

Example:

{{
  "security": 9,
  "scalability": 8,
  "reliability": 9,
  "cost": 7
}}

Return ONLY valid JSON.

Do not explain.

Do not use markdown.

Do not use code fences.

The response MUST exactly match:

{{
  "current_problems": "",
  "target_architecture": "",
  "migration_plan": "",
  "diagram": "",
  "scorecard": {{
    "security": 0,
    "scalability": 0,
    "reliability": 0,
    "cost": 0
  }}
}}
"""

        response = self.ollama.chat(prompt)

        return response
