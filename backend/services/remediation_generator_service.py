import json
import re


class RemediationGeneratorService:

    def __init__(
        self,
        provider
    ):

        self.provider = provider
    
    def generate(
        self,
        findings,
        knowledge_context
    ):

        remediations = []

        for finding in findings:

            print(
                f"Generating remediation for: {finding}"
            )

            remediation = (
                self.generate_single_remediation(
                    finding,
                    knowledge_context
                )
            )

            remediations.append(
                remediation
            )

        return {
            "remediations":
                remediations
        }
    
    def generate_single_remediation(
        self,
        finding,
        knowledge_context
    ):

        prompt = f"""
    You are a Principal Cloud Architect.

    Finding:

    {finding}

    Best Practices:

    {knowledge_context}

    IMPORTANT:

    Return ONLY JSON.

    Do not include:
    - Here is the output
    - Explanations
    - Notes
    - Markdown

    The first character of your response must be '['.
    The last character of your response must be ']'.

    {{
        "finding": "string",
        "priority": "high|medium|low",
        "remediation": "string",
        "implementation_steps": [
            "string"
        ]
    }}
    """

        response = (
            self.provider.generate(
                prompt
            )
        )

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print("RAW RESPONSE:")
        print(response)

        try:

            data = json.loads(
                response
            )

            if isinstance(
                data,
                list
            ):

                if len(data) > 0:

                    return data[0]

        except Exception as ex:

            print(
                f"Failed remediation for: {finding}"
            )

            print(ex)

            return {
                "finding": finding,
                "priority": "unknown",
                "remediation": "Unable to generate remediation",
                "implementation_steps": [
                    "Review the finding manually",
                    "Generate remediation again"
                ]
            }