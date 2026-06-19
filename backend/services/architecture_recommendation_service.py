import json
import re


class ArchitectureRecommendationService:
    def __init__(self, provider):

        self.provider = provider

    def generate(
        self,
        findings,
        risk_scores,
        benchmark_result,
        compliance_result,
        knowledge_context,
    ):

        findings_text = "\n".join(
            str(getattr(finding, "message", finding)) for finding in findings
        )

        prompt = f"""
You are a Principal Cloud Architect.

Current Findings:

{findings_text}

Risk Scores:

{json.dumps(risk_scores, indent=2)}

Benchmark Results:

{json.dumps(benchmark_result, indent=2)}

Compliance Results:

{json.dumps(compliance_result, indent=2)}

Knowledge Base:

{knowledge_context}

Generate:

1. Target architecture
2. Top recommendations
3. Expected improvements

IMPORTANT:

Generate REAL recommendations.

Do NOT generate JSON schemas.

Do NOT generate field definitions.

Do NOT generate property definitions.

Do not use markdown.

Do not use **bold** formatting.

Do not use bullet characters (*).

Return plain text only.

Do NOT use:

- $schema
- type
- properties
- required
- items

Return ACTUAL values.

Example:

{{
  "target_architecture":
    "Deploy workloads in a private Kubernetes cluster with HPA and secure networking.",

  "recommendations": [
    {{
      "priority": "High",
      "recommendation": "Enable Horizontal Pod Autoscaler",
      "benefit": "Improves scalability and reduces infrastructure costs"
    }}
  ],

  "expected_improvements": {{
    "security": "+30%",
    "reliability": "+25%",
    "scalability": "+40%"
  }}
}}
Generate recommendations now.
"""

        response = self.provider.generate(prompt)

        response = response.replace("```json", "").replace("```", "").strip()

        try:
            print("RECOMMENDATION RESPONSE:")
            print(response)

            match = re.search(r"\{.*\}", response, re.DOTALL)

            if match:
                result = json.loads(match.group(0))
                target_architecture = result.get("target_architecture", "")

                if isinstance(target_architecture, dict):
                    description = target_architecture.get("description", "")

                    components = ", ".join(target_architecture.get("components", []))

                    configurations = ", ".join(
                        target_architecture.get("configurations", [])
                    )

                    result["target_architecture"] = (
                        f"{description}\n\n"
                        f"Components: {components}\n\n"
                        f"Configurations: {configurations}"
                    )
                return result

            return {
                "target_architecture": response,
                "recommendations": [],
                "expected_improvements": {},
            }

        except Exception as ex:
            print("RECOMMENDATION JSON ERROR:")

            print(ex)

            print(response)

            return {
                "target_architecture": response,
                "recommendations": [],
                "expected_improvements": {},
            }
