class RiskScoringService:
    SECURITY_FINDINGS = {
        "Public EC2 instance detected": 15,
        "Public S3 bucket detected": 15,
        "IAM wildcard permissions detected": 15,
        "Hardcoded secrets detected": 20,
        "Public security group detected": 15,
        "Sensitive port 22 exposed": 10,
        "Sensitive port 3389 exposed": 10,
        "Public ingress combined with public security groups": 15,
        "Public cloud storage detected": 15,
    }

    RELIABILITY_FINDINGS = {
        "Missing liveness probe": 10,
        "Missing readiness probe": 10,
        "CPU limits not configured": 5,
        "CPU requests not configured": 5,
        "Memory requests not configured": 5,
        "Memory limits not configured": 5,
        "Container image uses latest tag": 5,
        "Resource tagging not detected": 5,
    }

    SCALABILITY_FINDINGS = {
        "No Horizontal Pod Autoscaler configured": 10,
        "Single replica deployment": 10,
        "No pod anti-affinity configured": 5,
        "No tolerations configured": 5,
    }

    def calculate(self, findings):

        security_score = 100
        reliability_score = 100
        scalability_score = 100

        for finding in findings:
            if finding in self.SECURITY_FINDINGS:
                security_score -= self.SECURITY_FINDINGS[finding]

            if finding in self.RELIABILITY_FINDINGS:
                reliability_score -= self.RELIABILITY_FINDINGS[finding]

            if finding in self.SCALABILITY_FINDINGS:
                scalability_score -= self.SCALABILITY_FINDINGS[finding]

        security_score = max(security_score, 0)

        reliability_score = max(reliability_score, 0)

        scalability_score = max(scalability_score, 0)

        overall_score = int(
            (security_score + reliability_score + scalability_score) / 3
        )

        maturity_level = self._calculate_maturity(overall_score)

        risk_level = self._calculate_risk(overall_score)

        return {
            "overall_score": overall_score,
            "security_score": security_score,
            "reliability_score": reliability_score,
            "scalability_score": scalability_score,
            "maturity_level": maturity_level,
            "risk_level": risk_level,
        }

    def _calculate_maturity(self, score):

        if score >= 90:
            return "Optimized"

        elif score >= 75:
            return "Managed"

        elif score >= 60:
            return "Developing"

        return "Initial"

    def _calculate_risk(self, score):

        if score >= 80:
            return "Low"

        elif score >= 60:
            return "Medium"

        return "High"
