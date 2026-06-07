class ReportAgent:

    def generate(
        self,
        result
    ):
        result.calculate_overall_score()
        return {

            "overall_score":
                result.overall_score,
            
            "risk_level": result.get_risk_level(),

            "category_scores":
                result.category_scores,

            "findings": [
                vars(f)
                for f in result.findings
            ],

            "recommendations": [
                vars(r)
                for r in result.recommendations
            ]
        }