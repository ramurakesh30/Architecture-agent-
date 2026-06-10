import json
import re
from urllib import response

from backend.app.providers.provider_factory import (
    ProviderFactory
)


def architect_node(
    state
):
    provider = (
        ProviderFactory.create()
    )

    prompt = f"""
You are a Principal Cloud Architect.

Security Assessment:

{state['security_review']}

Reliability Assessment:

{state['reliability_review']}

Scalability Assessment:

{state['scalability_review']}

Relevant Best Practices:

{state['knowledge_context']}

IMPORTANT:

Return ONLY valid JSON.

Use this schema:

{{
  "executive_assessment": "string",

  "top_priorities": [
    "string"
  ],

  "remediation_roadmap": [
    {{
      "name": "string",
      "description": "string",
      "steps": [
        "string"
      ],
      "timeline": "Short-term"
    }}
  ]
}}
"""

    result = (
        provider.generate(
            prompt
        )
    )
    print("CHIEF ARCHITECT RESPONSE:")
    print(result)
    
    match = re.search(
        r'\{.*\}',
        result,
        re.DOTALL
    )

    if match:

        try:

            state["final_review"] = (
                json.loads(
                    match.group(0)
                )
            )

        except Exception as ex:

            print(
                "CHIEF ARCHITECT JSON ERROR"
            )

            print(ex)

            state["final_review"] = {
                "executive_assessment":
                    result,

                "top_priorities": [],

                "remediation_roadmap": []
            }

    else:

        print(
            "NO JSON FOUND IN CHIEF ARCHITECT RESPONSE"
        )

        print(result)

        state["final_review"] = {
            "executive_assessment":
                result,

            "top_priorities": [],

            "remediation_roadmap": []
        }

    return state