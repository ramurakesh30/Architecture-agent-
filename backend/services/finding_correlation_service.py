class FindingCorrelationService:
    def deduplicate(self, result):

        # Findings
        unique_findings = []
        finding_keys = set()

        for finding in result.findings:
            key = (finding.category, finding.message)

            if key not in finding_keys:
                finding_keys.add(key)

                unique_findings.append(finding)

        result.findings = unique_findings

        # Recommendations
        unique_recommendations = []
        recommendation_keys = set()

        for recommendation in result.recommendations:
            key = (recommendation.category, recommendation.message)

            if key not in recommendation_keys:
                recommendation_keys.add(key)

                unique_recommendations.append(recommendation)

        result.recommendations = unique_recommendations

        return result
