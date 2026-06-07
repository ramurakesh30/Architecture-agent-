from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class KubernetesAgent:

    def analyze(self, request, result):

        if request.kubernetes is None:
            return

        k8s = request.kubernetes

        if not k8s.has_liveness_probe:


            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Missing liveness probe"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY,
                    message="Configure liveness probes"
                )
            )

        if not k8s.has_readiness_probe:


            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Missing readiness probe"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY,
                    message="Configure readiness probes"
                )
            )

        if not k8s.cpu_limit:


            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="CPU limits not configured"
                )
            )

        if not k8s.memory_limit:


            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="Memory limits not configured"
                )
            )