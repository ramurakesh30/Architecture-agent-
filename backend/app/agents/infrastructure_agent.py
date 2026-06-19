from app.domain.findings import Category, Finding, Recommendation, Severity


class InfrastructureAgent:
    def analyze(self, package, summary, result):

        self._check_scalability(summary, result)

        self._check_public_exposure(summary, result)

        self._check_storage_security(summary, result)

        self._check_high_availability(summary, result)

    def _check_scalability(self, summary, result):

        if summary.total_replicas < 3 and not summary.uses_hpa:
            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.CRITICAL,
                    message=("Infrastructure lacks automatic scaling capability"),
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SCALABILITY,
                    message=("Configure HPA and increase replica count"),
                )
            )

    def _check_public_exposure(self, summary, result):

        if summary.has_ingress and summary.public_security_groups > 0:
            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message=("Public ingress combined with public security groups"),
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY,
                    message=("Review ingress exposure and restrict security groups"),
                )
            )

    def _check_storage_security(self, summary, result):

        if summary.public_s3_buckets > 0:
            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message=("Public cloud storage detected"),
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY,
                    message=("Restrict public bucket access"),
                )
            )

    def _check_high_availability(self, summary, result):

        if summary.total_replicas < 3:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message=(
                        "Infrastructure may not meet high availability requirements"
                    ),
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY,
                    message=("Deploy at least three replicas across multiple nodes"),
                )
            )
