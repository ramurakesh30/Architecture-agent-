from fastapi import APIRouter

from uuid import UUID

from fastapi import (
    HTTPException
)

from services.report_repository import (
    ReportRepository
)

db_report_router = APIRouter()

repository = (
    ReportRepository()
)


@db_report_router.get(
    "/reports"
)
def list_reports():

    reports = (
        repository
        .list_reports()
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
def get_trends():

    return (
        repository
        .get_trends()
    )

@db_report_router.get(
    "/reports/{report_id}"
)
def get_report(
    report_id: str
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
            report_id
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
