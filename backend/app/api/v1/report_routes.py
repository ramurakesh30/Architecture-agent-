from fastapi import APIRouter, Depends

from uuid import UUID

from fastapi import (
    HTTPException
)

from services.report_repository import (
    ReportRepository
)

from backend.services.auth_dependency import (
    get_current_user_id
)

db_report_router = APIRouter()

repository = (
    ReportRepository()
)


@db_report_router.get(
    "/reports"
)
def list_reports(
    current_user_id: str = Depends(
        get_current_user_id
    )
):

    reports = (
        repository
        .list_reports(current_user_id)
    )

    return [

        {

            "id":
            str(report.id),

            "repository_name":
            report.repository_name,

            "overall_score":
            report.overall_score,

            "created_at":
            report.created_at
        }

        for report in reports
    ]

@db_report_router.get(
    "/reports/trends"
)
def get_trends(
    
    current_user_id: str = Depends(
        get_current_user_id
    )
):

    return (
        repository
        .get_trends(current_user_id)
    )

@db_report_router.get(
    "/reports/compare"
)
def compare_reports(

    report_a_id: str,

    report_b_id: str,

    current_user_id: str = Depends(
        get_current_user_id
    )
):

    return (

        repository
        .compare_reports(

            report_a_id,

            report_b_id,
            
            current_user_id
        )
    )


@db_report_router.get(
    "/reports/{report_id}"
)
def get_report(
    report_id: str,
    current_user_id: str = Depends(
        get_current_user_id
    )
):

    try:

        UUID(
            report_id
        )

    except ValueError:

        raise HTTPException(

            status_code=400,

            detail=
            "Invalid report id"
        )

    report = (
        repository
        .get_report(
            report_id,
            current_user_id
        )
    )

    if not report:

        raise HTTPException(

            status_code=404,

            detail=
            "Report not found"
        )

    return (
        report
        .report_json
    )

