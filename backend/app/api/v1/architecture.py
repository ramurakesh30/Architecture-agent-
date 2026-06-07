from fastapi import APIRouter

from backend.schemas.architecture import (
    ArchitectureRequest
)

from backend.services.architecture_review import (
    ArchitectureReviewService
)

router = APIRouter()

service = ArchitectureReviewService()


@router.post("/review")
def review_architecture(
    request: ArchitectureRequest
):
    result = service.analyze(
        request
    )

    return result