from backend.app.agents.availability_agent import AvailabilityAgent
from backend.app.agents.cloud_cost_agent import CloudCostAgent
from backend.app.agents.scalability_agent import ScalabilityAgent
from backend.app.agents.security_agent import SecurityAgent

from backend.app.agents.kubernetes_agent import KubernetesAgent
from backend.app.agents.report_agent import ReportAgent
from backend.app.agents.terraform_agent import TerraformAgent
from backend.app.domain.review_results import ReviewResult


class ArchitectureReviewService:
    def __init__(self):

        self.availability_agent = AvailabilityAgent()

        self.security_agent = SecurityAgent()

        self.scalability_agent = ScalabilityAgent()

        self.report_agent = ReportAgent()
        self.kubernetes_agent = KubernetesAgent()
        self.terraform_agent = TerraformAgent()
        self.cloud_cost_agent = CloudCostAgent()

    def analyze(self, request):

        result = ReviewResult()

        self.availability_agent.analyze(request, result)

        self.security_agent.analyze(request, result)

        self.scalability_agent.analyze(request, result)
        self.kubernetes_agent.analyze(request, result)

        self.terraform_agent.analyze(request, result)

        self.cloud_cost_agent.analyze(request, result)
        return self.report_agent.generate(result)
