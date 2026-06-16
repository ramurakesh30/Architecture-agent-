from db.database import (
    SessionLocal
)

from db.models import (
    AssessmentReport
)


class ReportRepository:

    def save(
        self,
        repository_name,
        overall_score,
        report
    ):

        db = SessionLocal()

        try:

            entity = (
                AssessmentReport(
                    repository_name=
                    repository_name,

                    overall_score=
                    overall_score,

                    report_json=
                    report
                )
            )

            db.add(
                entity
            )

            db.commit()

            db.refresh(
                entity
            )

            return str(
                entity.id
            )

        finally:

            db.close()

    def list_reports(
        self
    ):

        db = SessionLocal()

        try:

            return (

                db.query(
                    AssessmentReport
                )

                .order_by(
                    AssessmentReport
                    .created_at
                    .desc()
                )

                .all()
            )

        finally:

            db.close()

    def get_report(
        self,
        report_id
    ):

        db = SessionLocal()

        try:

            return (

                db.query(
                    AssessmentReport
                )

                .filter(
                    AssessmentReport.id
                    == report_id
                )

                .first()
            )

        finally:

            db.close()

    def get_trends(
        self
    ):

        db = SessionLocal()

        try:

            reports = (

                db.query(
                    AssessmentReport
                )

                .order_by(
                    AssessmentReport.created_at
                )

                .all()
            )

            return [

                {

                    "date":
                    report.created_at.strftime(
                        "%Y-%m-%d"
                    ),

                    "score":
                    report.overall_score
                }

                for report in reports
            ]

        finally:

            db.close()