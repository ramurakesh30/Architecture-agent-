from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class AvailabilityAgent:

    def analyze(
        self,
        request,
        result
    ):

        if request.replicas < 2:


            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Single point of failure detected"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY,
                    message="Increase replicas to at least 3"
                )
            )