from fastapi import APIRouter, File, UploadFile

from backend.app.agents.terraform_agent import TerraformAgent
from backend.app.parsers.terraform_parser import TerraformParser
from backend.services.terraform_review_service import TerraformReviewService

terraform_router = APIRouter()

parser = TerraformParser()

agent = TerraformAgent()

service = TerraformReviewService()


@terraform_router.post("/terraform/analyze")
async def analyze_terraform(file: UploadFile = File(...)):

    content = await file.read()

    return service.analyze(content.decode("utf-8"))
