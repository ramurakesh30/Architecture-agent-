from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from backend.services.report_repository import (
    ReportRepository
)

from backend.services.remediation_service import (
    RemediationService
)

from backend.services.auth_dependency import (
    get_current_user_id
)

router = APIRouter()

repository = ReportRepository()

remediation_service = (
    RemediationService()
)


@router.post(
    "/reports/{report_id}/remediation"
)
def generate_remediation_plan(

    report_id: str,

    current_user_id: str = Depends(
        get_current_user_id
    )

):

    report = (

        repository.get_report_by_id(

            report_id,

            current_user_id

        )

    )

    if not report:

        raise HTTPException(

            status_code=404,

            detail="Report not found"

        )

    remediation_plan = (

        remediation_service
        .generate_plan(

            report.report_json

        )

    )

    return remediation_plan