class ComplianceService:
    SOC2_CONTROLS = {
        "Hardcoded secrets detected": "Secrets Management",
        "IAM wildcard permissions detected": "Access Control",
        "Public S3 bucket detected": "Data Protection",
        "Public cloud storage detected": "Data Protection",
        "Public security group detected": "Network Security",
    }

    NIST_CONTROLS = {
        "IAM wildcard permissions detected": "Identity Management",
        "Hardcoded secrets detected": "Credential Management",
        "Public security group detected": "Network Protection",
        "Sensitive port 22 exposed": "Access Restrictions",
        "Sensitive port 3389 exposed": "Access Restrictions",
    }

    CIS_CONTROLS = {
        "Missing liveness probe": "Workload Health",
        "Missing readiness probe": "Workload Readiness",
        "No security context configured": "Pod Security",
        "No pod anti-affinity configured": "High Availability",
        "No tolerations configured": "Workload Scheduling",
    }

    ISO27001_CONTROLS = {
        "Hardcoded secrets detected": "Cryptographic Controls",
        "IAM wildcard permissions detected": "Access Management",
        "Public cloud storage detected": "Information Protection",
        "Public EC2 instance detected": "Network Security",
    }

    def assess(self, findings):

        finding_texts = []

        for finding in findings:
            if hasattr(finding, "message"):
                finding_texts.append(finding.message)

            else:
                finding_texts.append(str(finding))

        soc2 = self._evaluate(finding_texts, self.SOC2_CONTROLS, "SOC 2")

        nist = self._evaluate(finding_texts, self.NIST_CONTROLS, "NIST")

        cis = self._evaluate(finding_texts, self.CIS_CONTROLS, "CIS Kubernetes")

        iso = self._evaluate(finding_texts, self.ISO27001_CONTROLS, "ISO 27001")

        return {"frameworks": [soc2, nist, cis, iso]}

    def _evaluate(self, findings, controls, framework_name):

        total_controls = len(controls)

        failed_controls = []

        passed_controls = 0

        for finding_name, control_name in controls.items():
            found = any(finding_name.lower() in finding.lower() for finding in findings)

            if found:
                failed_controls.append(control_name)

            else:
                passed_controls += 1

        score = (
            int((passed_controls / total_controls) * 100) if total_controls > 0 else 0
        )

        return {
            "name": framework_name,
            "score": score,
            "passed_controls": passed_controls,
            "total_controls": total_controls,
            "failed_controls": failed_controls,
        }
