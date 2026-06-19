from fastapi import APIRouter, Depends, HTTPException

from backend.services.auth_dependency import get_current_user_id
from backend.services.diagram_service import DiagramService
from backend.services.report_repository import ReportRepository

router = APIRouter()

repository = ReportRepository()

diagram_service = DiagramService()


@router.post("/reports/{report_id}/diagram")
def generate_diagram(
    report_id: str, current_user_id: str = Depends(get_current_user_id)
):

    report = repository.get_report(report_id, current_user_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return diagram_service.generate_diagram(report.report_json)
