from dataclasses import dataclass, field

from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    SEVERITY_WEIGHTS
)


@dataclass
class ReviewResult:
    overall_score: int = 100

    category_scores: dict = field(
        default_factory=lambda: {
            Category.SECURITY.value: 100,
            Category.AVAILABILITY.value: 100,
            Category.SCALABILITY.value: 100,
            Category.COST.value: 100,
            Category.RELIABILITY.value: 100,
            Category.OBSERVABILITY.value: 100
        }
    )
    findings: list = field(default_factory=list)
    recommendations: list = field(default_factory=list)

    def add_finding(self, finding: Finding):
        penalty = SEVERITY_WEIGHTS[finding.severity]
        
        self.findings.append(finding)
        
        category = finding.category.value

        self.category_scores[
            category
        ] = max(
            0,
            self.category_scores[category]
            - penalty
        )

    def add_recommendation(self, recommendation: Recommendation):
        self.recommendations.append(recommendation)
    
    def calculate_overall_score(self):

        scores = list(
            self.category_scores.values()
        )

        self.overall_score = int(
            sum(scores) / len(scores)
        )

        return self.overall_score
    
    def get_risk_level(self):

        if self.overall_score >= 90:
            return "LOW"

        if self.overall_score >= 70:
            return "MEDIUM"

        if self.overall_score >= 50:
            return "HIGH"

        return "CRITICAL"