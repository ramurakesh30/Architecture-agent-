from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from backend.models.github_request import GithubRepositoryRequest
from backend.services.archive_service import ArchiveService
from backend.services.file_discovery_service import DiscoveryService
from backend.services.github_service import GithubService
from backend.services.infrastructure_review_service import (
    ArchitectureReviewService
)
from services.report_repository import (
    ReportRepository
)
from backend.services.auth_dependency import (
    get_current_user_id
)


import tempfile
import os


infrastructure_router = APIRouter()

archive_service = ArchiveService()

discovery_service = DiscoveryService()

review_service = ArchitectureReviewService()

@infrastructure_router.post("/architecture/analyze")
async def analyze_architecture(
    file: UploadFile = File(...),
     current_user_id: str = Depends(
        get_current_user_id
    )
):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".zip"
    )

    try:

        content = await file.read()

        temp_file.write(content)

        temp_file.close()

        extracted_dir = (
            archive_service.extract(
                temp_file.name
            )
        )

        files = (
            discovery_service.discover(
                extracted_dir
            )
        )

        report = (
            review_service.analyze(
            files
            )
        )

        repository = ReportRepository()

        repository.save(

            repository_name=
            file.filename,

            overall_score=
            report[
                "benchmark_result"
            ][
                "overall_score"
            ],

            report=
            report,
            
            user_id=
            current_user_id
        )

        return {
            "report": report
        }

    finally:

        if os.path.exists(
            temp_file.name
        ):
            os.remove(
                temp_file.name
            )

@infrastructure_router.post(
    "/analyze-github"
)
async def analyze_github_repository(
    request:
    GithubRepositoryRequest,
    
    current_user_id: str = Depends(
        get_current_user_id
    )
):

    github_service = (
        GithubService()
    )

    repo_path = (
        github_service
        .clone_repository(
            request.repository_url
        )
    )

    try:
        files = []

        for root, _, filenames in os.walk(repo_path):

            for filename in filenames:

                files.append(

                    os.path.join(
                        root,
                        filename
                    )
                )

        report = (

            review_service
            .analyze(
                files
            )
        )

        repository = ReportRepository()

        repository.save(
            repository_name=
            request.repository_url,

            overall_score=
            report[
                "benchmark_result"
            ][
                "overall_score"
            ],

            report=
            report,
            
            user_id=
            current_user_id
        )

        return report

    finally:

        github_service.cleanup(
            repo_path
        )