class NarrativeSummaryService:

    def generate(
        self,
        result
    ):

        findings = [
            f.message
            for f in result.findings
        ]

        summary_parts = []

        if (
            "Public S3 bucket detected"
            in findings
        ):

            summary_parts.append(
                "public cloud storage"
            )

        if (
            "IAM wildcard permissions detected"
            in findings
        ):

            summary_parts.append(
                "overly permissive IAM permissions"
            )

        if (
            "Hardcoded secrets detected"
            in findings
        ):

            summary_parts.append(
                "hardcoded credentials"
            )

        if (
            "Public security group detected"
            in findings
        ):

            summary_parts.append(
                "public network exposure"
            )

        security_text = ""

        if summary_parts:

            security_text = (
                "Critical security risks include "
                + ", ".join(summary_parts)
                + "."
            )

        return security_text