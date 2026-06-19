from backend.app.domain.findings import Category, Finding, Recommendation, Severity


class KubernetesAgent:
    def analyze(self, request, result):

        if request is None:
            return

        k8s = request

        if not k8s.has_liveness_probe:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Missing liveness probe",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY, message="Configure liveness probes"
                )
            )

        if not k8s.has_readiness_probe:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Missing readiness probe",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY, message="Configure readiness probes"
                )
            )

        if not k8s.cpu_limit:
            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="CPU limits not configured",
                )
            )
        if not k8s.cpu_request:
            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="CPU requests not configured",
                )
            )
        if not k8s.memory_request:
            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="Memory requests not configured",
                )
            )

        if not k8s.memory_limit:
            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.MEDIUM,
                    message="Memory limits not configured",
                )
            )
        if not k8s.has_security_context:
            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.HIGH,
                    message="No security context configured",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY, message="Run containers as non-root"
                )
            )
        if not k8s.has_affinity_rules:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.MEDIUM,
                    message="No pod anti-affinity configured",
                )
            )
        if not k8s.has_tolerations:
            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.LOW,
                    message="No tolerations configured",
                )
            )

        if not k8s.has_hpa:
            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.MEDIUM,
                    message="No Horizontal Pod Autoscaler configured",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SCALABILITY,
                    message="Configure HPA for automatic scaling",
                )
            )

        if not k8s.has_ingress:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.LOW,
                    message="No ingress resource detected",
                )
            )

        if k8s.replicas < 2:
            result.add_finding(
                Finding(
                    category=Category.AVAILABILITY,
                    severity=Severity.HIGH,
                    message="Single replica deployment",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.AVAILABILITY, message="Use at least 3 replicas"
                )
            )

        for tag in k8s.image_tags:
            if tag == "latest":
                result.add_finding(
                    Finding(
                        category=Category.RELIABILITY,
                        severity=Severity.MEDIUM,
                        message="Container image uses latest tag",
                    )
                )

                result.add_recommendation(
                    Recommendation(
                        category=Category.RELIABILITY,
                        message="Use immutable version tags",
                    )
                )
        if k8s.container_count > 3:
            result.add_finding(
                Finding(
                    category=Category.SCALABILITY,
                    severity=Severity.MEDIUM,
                    message=f"Pod contains {k8s.container_count} containers",
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SCALABILITY,
                    message="Reduce container count or split workloads",
                )
            )
