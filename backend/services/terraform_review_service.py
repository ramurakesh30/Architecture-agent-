from backend.app.parsers.terraform_parser import TerraformParser
from backend.app.agents.terraform_agent import TerraformAgent
from backend.app.domain.review_results import ReviewResult


class TerraformReviewService:

    def __init__(self):

        self.parser = TerraformParser()

        self.agent = TerraformAgent()

    def analyze(
        self,
        tf_content: str
    ):

        config = self.parser.parse(
            tf_content
        )

        result = ReviewResult()

        self.agent.analyze(
            config,
            result
        )

        result.calculate_overall_score()

        return {
            "overall_score":
                result.overall_score,

            "category_scores":
                result.category_scores,

            "findings":
                [vars(f) for f in result.findings],

            "recommendations":
                [vars(r) for r in result.recommendations]
        }