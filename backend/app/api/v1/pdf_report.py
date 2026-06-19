import tempfile

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse

from backend.services.archive_service import ArchiveService
from backend.services.file_discovery_service import DiscoveryService
from backend.services.infrastructure_review_service import ArchitectureReviewService
from backend.services.pdf_report_service import PdfReportService

pdf_report_router = APIRouter()

pdf_service = PdfReportService()

archive_service = ArchiveService()

discovery_service = DiscoveryService()

review_service = ArchitectureReviewService()


@pdf_report_router.post("/architecture/report")
async def generate_report(file: UploadFile = File(...)):

    temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")

    try:
        content = await file.read()

        temp_zip.write(content)

        temp_zip.close()

        extracted_dir = archive_service.extract(temp_zip.name)

        files = discovery_service.discover(extracted_dir)

        report = review_service.analyze(files)

        pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

        pdf_file.close()

        pdf_service.generate(report, pdf_file.name)

        return FileResponse(
            pdf_file.name,
            media_type="application/pdf",
            filename="architecture-review.pdf",
        )

    finally:
        pass
