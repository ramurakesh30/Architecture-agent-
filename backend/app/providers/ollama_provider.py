import json
import re

from ollama import chat

from app.providers.ai_provider import (
    AIProvider
)


class OllamaProvider(
    AIProvider
):

    def __init__(
        self,
        model
    ):

        self.model = model

        print(f'the model is: {self.model}')

    def generate_architecture_review(
        self,
        findings,
        knowledge_context
    ):
        
        findings_text = "\n".join(
            findings
        )

        prompt = f"""
You are a Principal Cloud Architect.

Review these architecture findings.

ARCHITECTURE FINDINGS:

{findings_text}

RELEVANT BEST PRACTICES:

{knowledge_context}

IMPORTANT:

1. Use the provided best-practice knowledge when creating recommendations.
2. Reference industry-standard approaches where appropriate.
3. Return ONLY valid JSON.
4. Do not include markdown.
5. Do not include explanations outside JSON.
6. top_priorities must be an array of strings.
7. remediation_roadmap must be an array of objects.

Example:

{{
  "executive_assessment":
    "The platform contains significant security and availability risks.",

  "top_priorities": [
    "Remove public S3 access",
    "Implement HPA",
    "Configure readiness probes"
  ],

  "remediation_roadmap": [
    {{
      "name": "Secure Cloud Storage",

      "description":
        "Public S3 buckets expose sensitive information.",

      "steps": [
        "Enable Block Public Access",
        "Review bucket policies",
        "Enable encryption"
      ],

      "timeline": "Short-term"
    }}
  ]
}}

Generate:

1. Executive Assessment
2. Top Priorities
3. Remediation Roadmap

Use the best-practice knowledge provided above when generating recommendations.
"""

        response = chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response[
            "message"
        ][
            "content"
        ]

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )
        print("OLLAMA RESPONSE:")
        print(content)

        match = re.search(
            r'\{.*\}',
            content,
            re.DOTALL
        )

        if not match:

            raise ValueError(
                "No JSON found in model response"
            )

        json_text = match.group(0)

        return json.loads(
            json_text
        )
    
    def generate(
        self,
        prompt
    ):

        response = chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response[
            "message"
        ][
            "content"
        ]