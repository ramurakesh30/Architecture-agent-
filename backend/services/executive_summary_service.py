class ExecutiveSummaryService:
    
    def get_risk_level(
        self,
        score: int
    ):

        if score >= 90:
            return "LOW"

        if score >= 70:
            return "MEDIUM"

        if score >= 50:
            return "HIGH"

        return "CRITICAL"
    
    def get_top_risks(
        self,
        result
    ):

        severity_order = {
            "critical": 4,
            "high": 3,
            "medium": 2,
            "low": 1
        }

        findings = sorted(
            result.findings,
            key=lambda x:
                severity_order.get(
                    x.severity,
                    0
                ),
            reverse=True
        )

        return [
            finding.message
            for finding in findings[:5]
        ]
    
    def build_category_summary(
        self,
        result
        ):

        summary = {}

        for finding in result.findings:

            category = finding.category

            summary.setdefault(
                category,
                0
            )

            summary[category] += 1

        return summary
    
    def _build_summary(
        self,
        result
    ):

        security_count = 0
        availability_count = 0
        reliability_count = 0
        scalability_count = 0

        for finding in result.findings:

            category = finding.category

            # Handle Enum or string
            if hasattr(category, "value"):
                category = category.value

            if category == "security":
                security_count += 1

            elif category == "availability":
                availability_count += 1

            elif category == "reliability":
                reliability_count += 1

            elif category == "scalability":
                scalability_count += 1

        summary_parts = []

        if security_count:
            summary_parts.append(
                f"{security_count} security issues"
            )

        if availability_count:
            summary_parts.append(
                f"{availability_count} availability issues"
            )

        if reliability_count:
            summary_parts.append(
                f"{reliability_count} reliability issues"
            )

        if scalability_count:
            summary_parts.append(
                f"{scalability_count} scalability issues"
            )

        return (
            "Infrastructure assessment identified "
            + ", ".join(summary_parts)
            + "."
        )
    
    def generate(
        self,
        result
    ):

        return {

            "risk_level":
                self.get_risk_level(
                    result.overall_score
                ),

            "executive_summary":
                self._build_summary(
                    result
                ),

            "top_risks":
                self.get_top_risks(
                    result
                ),

            "category_summary":
                self.build_category_summary(
                    result
                )
        }
