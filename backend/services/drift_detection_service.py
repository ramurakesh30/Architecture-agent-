class DriftDetectionService:

    def compare(
        self,
        previous_findings,
        current_findings
    ):

        previous = set()

        current = set()

        for finding in previous_findings:

            if hasattr(
                finding,
                "message"
            ):

                previous.add(
                    finding.message
                )

            else:

                previous.add(
                    str(finding)
                )

        for finding in current_findings:

            if hasattr(
                finding,
                "message"
            ):

                current.add(
                    finding.message
                )

            else:

                current.add(
                    str(finding)
                )

        added_findings = list(

            current -
            previous
        )

        removed_findings = list(

            previous -
            current
        )

        return {

            "added_findings":
                sorted(
                    added_findings
                ),

            "removed_findings":
                sorted(
                    removed_findings
                ),

            "drift_detected":
                len(
                    added_findings
                ) > 0
                or
                len(
                    removed_findings
                ) > 0
        }