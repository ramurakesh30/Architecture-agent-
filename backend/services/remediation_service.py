class RemediationService:

    def generate_plan(
        self,
        report: dict
    ):

        findings = report.get(
            "findings",
            []
        )

        critical = []
        medium = []
        low = []

        for finding in findings:

            category = (
                finding.get(
                    "category",
                    ""
                )
                .lower()
            )

            severity = (
                finding.get(
                    "severity",
                    "low"
                )
                .lower()
            )

            recommendations = []

            if category == "security":

                recommendations.extend([

                    {
                        "recommendation":
                        "Review IAM permissions and remove wildcard access.",

                        "effort":
                        "1 day"
                    },

                    {
                        "recommendation":
                        "Enable encryption at rest for all storage services.",

                        "effort":
                        "1 day"
                    },

                    {
                        "recommendation":
                        "Enable audit logging and monitoring.",

                        "effort":
                        "2 days"
                    }

                ])

            elif category == "infrastructure":

                recommendations.extend([

                    {
                        "recommendation":
                        "Implement infrastructure as code validation checks.",

                        "effort":
                        "2 days"
                    },

                    {
                        "recommendation":
                        "Enable automated backups and disaster recovery validation.",

                        "effort":
                        "2 days"
                    }

                ])

            elif category == "architecture":

                recommendations.extend([

                    {
                        "recommendation":
                        "Reduce tight coupling between services.",

                        "effort":
                        "3 days"
                    },

                    {
                        "recommendation":
                        "Introduce clear service boundaries.",

                        "effort":
                        "3 days"
                    }

                ])

            else:

                recommendations.append(

                    {
                        "recommendation":
                        "Review finding and address identified issue.",

                        "effort":
                        "1 day"
                    }

                )

            if severity == "critical":

                critical.extend(
                    recommendations
                )

            elif severity == "medium":

                medium.extend(
                    recommendations
                )

            else:

                low.extend(
                    recommendations
                )

        return {

            "critical":
            critical,

            "medium":
            medium,

            "low":
            low

        }