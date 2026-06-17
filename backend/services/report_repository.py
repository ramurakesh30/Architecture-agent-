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
        report,
        user_id
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
                    report,

                    user_id=
                    user_id
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
        self,
        user_id
    ):

        db = SessionLocal()

        try:

            return (

                db.query(
                    AssessmentReport
                )
                .filter(
                    AssessmentReport.user_id
                    == user_id
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
        report_id,
        user_id
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
                
                .filter(
                    AssessmentReport.user_id
                    == user_id
                )

                .first()
            )

        finally:

            db.close()

    def get_trends(
        self,
        user_id
    ):

        db = SessionLocal()

        try:

            reports = (

                db.query(
                    AssessmentReport
                )
                
                .filter(
                    AssessmentReport.user_id
                    == user_id
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
    
    def compare_reports(
        self,
        report_a_id: str,
        report_b_id: str,
        user_id: str
    ):

        db = SessionLocal()

        try:

            report_a = (
                db.query(
                    AssessmentReport
                )
                .filter(
                    AssessmentReport.id
                    == report_a_id
                )
                .filter(
                    AssessmentReport.user_id
                    == user_id
                )
                .first()
            )

            report_b = (
                db.query(
                    AssessmentReport
                )
                .filter(
                    AssessmentReport.id
                    == report_b_id
                )
                .filter(
                    AssessmentReport.user_id
                    == user_id
                )
                .first()
            )

            return {

                "report_a":
                    report_a.report_json,

                "report_b":
                    report_b.report_json
            }

        finally:

            db.close()