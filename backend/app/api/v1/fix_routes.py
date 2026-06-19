from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from backend.services.auth_dependency import get_current_user_id
from backend.services.fix_generation_service import FixGenerationService
from backend.services.report_repository import ReportRepository

router = APIRouter()

repository = ReportRepository()

fix_service = FixGenerationService()


class FixRequest(BaseModel):
    finding: str


@router.post("/reports/{report_id}/fix")
def generate_fix(
    report_id: str,
    request: FixRequest,
    current_user_id: str = Depends(get_current_user_id),
):

    report = repository.get_report(report_id, current_user_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return fix_service.generate_fix(report.report_json, request.finding)
