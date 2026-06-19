class DashboardService:
    def build(self, report):

        return {
            "overall_score": report["overall_score"],
            "risk_level": report["risk_level"],
            "security_score": report["category_scores"]["security"],
            "availability_score": report["category_scores"]["availability"],
            "reliability_score": report["category_scores"]["reliability"],
            "scalability_score": report["category_scores"]["scalability"],
            "top_risks": report["top_risks"],
            "summary": report["narrative_summary"],
            "risk_breakdown": self.get_risk_breakdown(report),
        }

    def get_risk_breakdown(self, report):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for finding in report["findings"]:
            severity = finding["severity"]

            if severity == "critical":
                critical += 1

            elif severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            elif severity == "low":
                low += 1

        return {"critical": critical, "high": high, "medium": medium, "low": low}
