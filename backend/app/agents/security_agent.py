from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class SecurityAgent:

    def analyze(
        self,
        request,
        result
    ):

        if request.public_api:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.MEDIUM,
                    message="Public API detected"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY,
                    message="Protect APIs using API Gateway"
                )
            )