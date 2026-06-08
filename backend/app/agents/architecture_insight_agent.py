from app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)

class ArchitectureInsightAgent:

    def analyze(
        self,
        summary,
        result
    ):

        if (
            summary.total_replicas < 3
            and
            not summary.uses_hpa
        ):

            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.CRITICAL,
                    message=(
                        "Infrastructure is not highly "
                        "available and cannot scale"
                    )
                )
            )