from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.app.parsers.terraform_parser import TerraformParser
from backend.app.agents.terraform_agent import TerraformAgent
from backend.app.domain.review_results import ReviewResult
from backend.services.terraform_review_service import (
    TerraformReviewService
)

terraform_router = APIRouter()

parser = TerraformParser()

agent = TerraformAgent()

service = TerraformReviewService()

@terraform_router.post("/terraform/analyze")
async def analyze_terraform(
    file: UploadFile = File(...)
):

    content = await file.read()

    return service.analyze(
        content.decode("utf-8")
    )