import json
import re


class ArchitectureDocumentationService:

    def __init__(
        self,
        ai_review_service
    ):

        self.ai_review_service = (
            ai_review_service
        )

    def generate(
        self,
        summary
    ):

        prompt = f"""
You are a senior cloud architect.

Generate architecture documentation.

Infrastructure:

Deployments:
{summary.total_deployments}

Replicas:
{summary.total_replicas}

Has Ingress:
{summary.has_ingress}

Uses HPA:
{summary.uses_hpa}

Public Security Groups:
{summary.public_security_groups}

Public S3 Buckets:
{summary.public_s3_buckets}

IMPORTANT:

Return ONLY JSON.

All values MUST be strings.

Do NOT use arrays.
Do NOT use nested objects.

Example:

{{
  "overview":
    "The platform consists of three Kubernetes deployments exposed through an ingress controller.",

  "traffic_flow":
    "External HTTP traffic enters through the ingress and is routed to application deployments.",

  "scalability":
    "Horizontal Pod Autoscaling is not configured, limiting automatic scaling.",

  "security":
    "Public security groups and public cloud storage introduce significant security risks.",

  "operational_risks":
    "Single points of failure and missing autoscaling may affect application availability."
}}

Generate documentation now.
"""

        response = self.ai_review_service.ask(
            prompt
        )

        match = re.search(
            r'\{.*\}',
            response,
            re.DOTALL
        )

        if match:

            try:

                result = json.loads(
                    match.group(0)
                )

                #
                # Force all values to strings
                #

                for key in result:

                    if not isinstance(
                        result[key],
                        str
                    ):

                        result[key] = str(
                            result[key]
                        )

                return result

            except Exception as ex:

                print(
                    f"JSON parse failed: {ex}"
                )

        return {

            "overview": response,

            "traffic_flow": "",

            "scalability": "",

            "security": "",

            "operational_risks": ""
        }