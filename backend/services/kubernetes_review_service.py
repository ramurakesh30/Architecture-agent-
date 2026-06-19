from backend.app.agents.kubernetes_agent import KubernetesAgent
from backend.app.domain.review_results import ReviewResult
from backend.app.parsers.kubernetes_parser import KubernetesParser


class KubernetesReviewService:
    def __init__(self):

        self.parser = KubernetesParser()

        self.agent = KubernetesAgent()

    def analyze(self, yaml_content: str):

        config = self.parser.parse(yaml_content)

        result = ReviewResult()

        self.agent.analyze(config, result)

        result.calculate_overall_score()

        return result
