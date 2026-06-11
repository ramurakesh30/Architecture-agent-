class CostOptimizationService:

    RULES = {

        "No Horizontal Pod Autoscaler configured": {
            "recommendation":
                "Enable autoscaling to optimize resource consumption.",
            "impact":
                "High"
        },

        "CPU limits not configured": {
            "recommendation":
                "Define CPU limits to avoid overprovisioning.",
            "impact":
                "Medium"
        },

        "Memory limits not configured": {
            "recommendation":
                "Define memory limits to reduce wasted capacity.",
            "impact":
                "Medium"
        },

        "Single replica deployment": {
            "recommendation":
                "Review workload sizing and scaling strategy.",
            "impact":
                "Low"
        },

        "Container image uses latest tag": {
            "recommendation":
                "Use versioned images to improve deployment predictability.",
            "impact":
                "Low"
        }
    }

    def analyze(
        self,
        findings
    ):

        opportunities = []

        for finding in findings:

            if hasattr(
                finding,
                "message"
            ):

                finding_text = (
                    finding.message
                )

            else:

                finding_text = (
                    str(finding)
                )

            if (
                finding_text
                in self.RULES
            ):

                opportunities.append({

                    "finding":
                        finding_text,

                    "recommendation":
                        self.RULES[
                            finding_text
                        ][
                            "recommendation"
                        ],

                    "impact":
                        self.RULES[
                            finding_text
                        ][
                            "impact"
                        ]
                })

        return {

            "total_opportunities":
                len(
                    opportunities
                ),

            "opportunities":
                opportunities
        }