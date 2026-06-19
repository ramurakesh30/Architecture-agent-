from typing import TypedDict


class ReviewState(TypedDict):
    findings: list

    knowledge_context: str

    security_review: str

    reliability_review: str

    scalability_review: str

    cost_review: str

    final_review: dict
