import json


class ArchitectureDocumentationService:
    def __init__(self, ai_review_service):

        self.ai_review_service = ai_review_service

    def generate(self, summary):

        prompt = f"""
You are a Senior Cloud Architect.

Generate a concise architecture assessment.

Infrastructure:

Deployments: {summary.total_deployments}
Replicas: {summary.total_replicas}
Has Ingress: {summary.has_ingress}
Uses HPA: {summary.uses_hpa}
Public Security Groups: {summary.public_security_groups}
Public S3 Buckets: {summary.public_s3_buckets}

Return only a short architecture assessment paragraph.
Do not use headings.
Do not use markdown.
Do not use JSON.
"""

        response = self.ai_review_service.ask(prompt)

        response = response.replace("```json", "").replace("```", "").strip()
        print("DOCUMENTATION RESPONSE")
        print(response)

        json_start = response.find("{")

        if json_start >= 0:
            response = response[json_start:]
        try:
            decoder = json.JSONDecoder()

            result, idx = decoder.raw_decode(response)

            for key in result:
                if not isinstance(result[key], str):
                    result[key] = str(result[key])

            return result

        except Exception as ex:
            print(f"JSON parse failed: {ex}")

            print(response)

            return {
                "overview": response,
                "traffic_flow": f"Traffic enters through ingress and is routed across "
                f"{summary.total_deployments} deployments.",
                "scalability": f"HPA enabled: {summary.uses_hpa}. "
                f"Total replicas: {summary.total_replicas}.",
                "security": f"Public security groups: "
                f"{summary.public_security_groups}. "
                f"Public S3 buckets: "
                f"{summary.public_s3_buckets}.",
                "operational_risks": self._generate_operational_risks(summary),
            }

    def _generate_operational_risks(self, summary):

        risks = []

        if not summary.uses_hpa:
            risks.append("Autoscaling is not configured.")

        if summary.total_replicas <= 1:
            risks.append("Single replica deployment detected.")

        if summary.public_security_groups > 0:
            risks.append("Public network exposure exists.")

        return " ".join(risks)
