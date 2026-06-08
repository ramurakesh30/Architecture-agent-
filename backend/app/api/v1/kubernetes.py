from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.app.parsers.kubernetes_parser import KubernetesParser
from backend.app.agents.kubernetes_agent import KubernetesAgent
from backend.app.domain.review_results import ReviewResult
from backend.services.kubernetes_review_service import (
    KubernetesReviewService
)

kubernetes_router = APIRouter()

parser = KubernetesParser()

agent = KubernetesAgent()

service = KubernetesReviewService()

@kubernetes_router.post("/kubernetes/analyze")
async def analyze_kubernetes(
    file: UploadFile = File(...)
):

    content = await file.read()

    result = service.analyze(
        content.decode("utf-8")
    )

    return {
        "overall_score":
            result.overall_score,

        "category_scores":
            result.category_scores,

        "findings":
            [vars(f) for f in result.findings],

        "recommendations":
            [vars(r) for r in result.recommendations]
    }