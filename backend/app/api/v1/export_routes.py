import tempfile

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse

from backend.services.auth_dependency import get_current_user_id
from backend.services.pdf_report_service import PdfReportService
from backend.services.report_repository import ReportRepository

router = APIRouter()

repository = ReportRepository()

pdf_service = PdfReportService()


@router.get("/reports/{report_id}/pdf")
def export_report_pdf(
    report_id: str, current_user_id: str = Depends(get_current_user_id)
):

    report = repository.get_report(report_id, current_user_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf_file.close()

    pdf_service.generate(report.report_json, pdf_file.name)

    repository_name = report.repository_name.replace(" ", "_")

    return FileResponse(
        path=pdf_file.name,
        media_type="application/pdf",
        filename=f"{repository_name}_architecture_report.pdf",
    )
