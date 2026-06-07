from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class ScalabilityAgent:

    def analyze(
        self,
        request,
        result
    ):

        if len(request.services) > 10:

            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.MEDIUM,
                    message="High service count detected"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SCALABILITY,
                    message="Consider service mesh"
                )
            )