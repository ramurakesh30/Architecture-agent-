class BenchmarkService:
    AWS_CONTROLS = {
        "Public S3 bucket detected": "S3 Public Access Control",
        "Public cloud storage detected": "Cloud Storage Security",
        "IAM wildcard permissions detected": "Least Privilege IAM",
        "Hardcoded secrets detected": "Secrets Management",
        "Public security group detected": "Network Segmentation",
    }

    KUBERNETES_CONTROLS = {
        "Missing liveness probe": "Liveness Probe",
        "Missing readiness probe": "Readiness Probe",
        "No Horizontal Pod Autoscaler configured": "Horizontal Pod Autoscaler",
        "Single replica deployment": "High Availability",
        "No pod anti-affinity configured": "Pod Anti-Affinity",
        "No tolerations configured": "Node Tolerations",
    }

    SECURITY_CONTROLS = {
        "Public EC2 instance detected": "Private Compute Resources",
        "Sensitive port 22 exposed": "SSH Hardening",
        "Sensitive port 3389 exposed": "RDP Hardening",
        "Public ingress combined with public security groups": "Zero Trust Networking",
    }

    def benchmark(self, findings):

        finding_texts = []

        for finding in findings:
            if hasattr(finding, "message"):
                finding_texts.append(finding.message)

            else:
                finding_texts.append(str(finding))

        aws_result = self._evaluate_framework(
            finding_texts, self.AWS_CONTROLS, "AWS Well-Architected"
        )

        kubernetes_result = self._evaluate_framework(
            finding_texts, self.KUBERNETES_CONTROLS, "Kubernetes Best Practices"
        )

        security_result = self._evaluate_framework(
            finding_texts, self.SECURITY_CONTROLS, "Cloud Security Best Practices"
        )

        overall_score = int(
            (
                aws_result["score"]
                + kubernetes_result["score"]
                + security_result["score"]
            )
            / 3
        )

        failed_controls = (
            aws_result["failed_controls"]
            + kubernetes_result["failed_controls"]
            + security_result["failed_controls"]
        )

        return {
            "overall_score": overall_score,
            "frameworks": [aws_result, kubernetes_result, security_result],
            "failed_controls": failed_controls,
        }

    def _evaluate_framework(self, findings, controls, framework_name):

        total_controls = len(controls)

        failed_controls = []

        passed_controls = 0

        for finding in findings:
            print(finding)

        for finding_name, control_name in controls.items():
            found = any(finding_name.lower() in finding.lower() for finding in findings)

            print(f"{finding_name} -> {found}")

            if found:
                failed_controls.append(control_name)

            else:
                passed_controls += 1

            score = (
                max(20, int((passed_controls / total_controls) * 100))
                if total_controls > 0
                else 0
            )

        return {
            "name": framework_name,
            "score": score,
            "passed_controls": passed_controls,
            "total_controls": total_controls,
            "failed_controls": failed_controls,
        }
