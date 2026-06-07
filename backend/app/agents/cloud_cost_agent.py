from app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class CloudCostAgent:

    def analyze(self, request, result):

        if request.cloud is None:
            return

        cloud = request.cloud

        if not cloud.autoscaling_enabled:


            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.MEDIUM,
                    message="Autoscaling disabled"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SCALABILITY,
                    message="Enable autoscaling"
                )
            )

        if cloud.estimated_monthly_cost > 5000:

            result.add_finding(
                Finding(
                    category=Category.COST,
                    severity=Severity.MEDIUM,
                    message=f"High monthly cloud cost: €{cloud.estimated_monthly_cost}"
                )
            )