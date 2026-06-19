import os

from app.agents.architecture_insight_agent import ArchitectureInsightAgent
from app.agents.infrastructure_agent import InfrastructureAgent
from app.agents.kubernetes_agent import KubernetesAgent
from app.agents.terraform_agent import TerraformAgent
from app.config.settings import Settings
from app.domain.infrastructure import InfrastructurePackage
from app.domain.review_results import ReviewResult
from app.parsers.kubernetes_parser import KubernetesParser
from app.parsers.terraform_parser import TerraformParser
from app.providers.provider_factory import ProviderFactory

from backend.app.langgraph.review_graph import review_graph
from backend.services.ai_review_service import AIReviewService
from backend.services.architecture_diagram_service import ArchitectureDiagramService
from backend.services.architecture_documentation_service import (
    ArchitectureDocumentationService,
)
from backend.services.architecture_recommendation_service import (
    ArchitectureRecommendationService,
)
from backend.services.benchmark_service import BenchmarkService
from backend.services.compliance_service import ComplianceService
from backend.services.cost_optimization_service import CostOptimizationService
from backend.services.dashboard_service import DashboardService
from backend.services.diagram_renderer_service import DiagramRendererService
from backend.services.drift_detection_service import DriftDetectionService
from backend.services.executive_summary_service import ExecutiveSummaryService
from backend.services.finding_correlation_service import FindingCorrelationService
from backend.services.history_service import HistoryService
from backend.services.infrastructure_aggregator import InfrastructureAggregator
from backend.services.narrative_summary_service import NarrativeSummaryService
from backend.services.rag_service import RAGService
from backend.services.remediation_generator_service import RemediationGeneratorService
from backend.services.risk_scoring_service import RiskScoringService
from backend.services.vector_store_service import VectorStoreService


class ArchitectureReviewService:
    def __init__(self):

        self.kubernetes_parser = KubernetesParser()

        self.terraform_parser = TerraformParser()

        self.kubernetes_agent = KubernetesAgent()

        self.terraform_agent = TerraformAgent()

        self.infrastructure_agent = InfrastructureAgent()

        self.aggregator = InfrastructureAggregator()

        self.insight_agent = ArchitectureInsightAgent()

        self.correlation_service = FindingCorrelationService()

        self.executive_summary_service = ExecutiveSummaryService()

        self.diagram_service = ArchitectureDiagramService()

        self.diagram_renderer_service = DiagramRendererService()

        self.narrative_summary_service = NarrativeSummaryService()

        self.dashboard_service = DashboardService()

        provider = ProviderFactory.create()

        self.vector_store_service = VectorStoreService()

        self.vector_store_service.index_documents()

        self.rag_service = RAGService(self.vector_store_service)

        self.review_graph = review_graph

        self.ai_review_service = AIReviewService(provider)

        self.risk_scoring_service = RiskScoringService()

        self.architecture_documentation_service = ArchitectureDocumentationService(
            self.ai_review_service
        )

        self.benchmark_service = BenchmarkService()

        self.history_service = HistoryService()

        self.drift_service = DriftDetectionService()

        self.cost_optimization_service = CostOptimizationService()

        self.compliance_service = ComplianceService()

        self.recommendation_service = ArchitectureRecommendationService(provider)

    def analyze(self, files):

        package = InfrastructurePackage()

        for file in files:
            extension = os.path.splitext(file)[1].lower()

            if extension not in Settings.SUPPORTED_EXTENSIONS:
                continue

            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()

            except UnicodeDecodeError:
                continue

            if file.endswith((".yaml", ".yml")):
                package.kubernetes_configs.append(self.kubernetes_parser.parse(content))

            elif file.endswith(".tf"):
                package.terraform_configs.append(self.terraform_parser.parse(content))

        result = ReviewResult()

        for k8s in package.kubernetes_configs:
            self.kubernetes_agent.analyze(k8s, result)

        for tf in package.terraform_configs:
            self.terraform_agent.analyze(tf, result)
        summary = self.aggregator.summarize(package)

        self.infrastructure_agent.analyze(package, summary, result)
        self.insight_agent.analyze(summary, result)
        result = self.correlation_service.deduplicate(result)

        result.calculate_overall_score()

        findings = [f.message for f in result.findings][:3]

        self.remediation_generator_service = RemediationGeneratorService(
            ProviderFactory.create()
        )

        risk_scores = self.risk_scoring_service.calculate(
            [f.message for f in result.findings]
        )

        knowledge_context = self.rag_service.enrich(result.findings)

        remediation_code = self.remediation_generator_service.generate(
            findings, knowledge_context
        )

        graph_result = self.review_graph.invoke(
            {"findings": result.findings, "knowledge_context": knowledge_context}
        )

        ai_architecture_review = graph_result["final_review"]

        summary_report = self.executive_summary_service.generate(result)

        diagram = self.diagram_service.generate(summary)

        # diagram_image = (
        #     self.diagram_renderer_service
        #     .render(
        #         diagram,
        #        "architecture.png"
        #    )
        # )

        architecture_documentation = self.architecture_documentation_service.generate(
            summary
        )

        benchmark_result = self.benchmark_service.benchmark(result.findings)

        previous_findings = self.history_service.load_latest()

        drift_result = self.drift_service.compare(previous_findings, result.findings)

        cost_result = self.cost_optimization_service.analyze(result.findings)

        compliance_result = self.compliance_service.assess(result.findings)

        print("COMPLIANCE RESULT:")
        print(compliance_result)

        self.history_service.save(result.findings)

        recommendation_result = self.recommendation_service.generate(
            result.findings,
            risk_scores,
            benchmark_result,
            compliance_result,
            knowledge_context,
        )

        narrative_summary = self.narrative_summary_service.generate(result)

        dashboard = self.dashboard_service.build(
            {
                "overall_score": result.overall_score,
                "risk_level": summary_report["risk_level"],
                "category_scores": result.category_scores,
                "top_risks": summary_report["top_risks"],
                "narrative_summary": narrative_summary,
                "findings": [vars(f) for f in result.findings],
            }
        )

        return {
            "overall_score": result.overall_score,
            "risk_level": summary_report["risk_level"],
            "executive_summary": summary_report["executive_summary"],
            "architecture_diagram": diagram,
            # "architecture_diagram_image":
            # diagram_image,
            "architecture_documentation": architecture_documentation,
            "narrative_summary": narrative_summary,
            "top_risks": summary_report["top_risks"],
            "category_summary": summary_report["category_summary"],
            "dashboard": dashboard,
            "risk_scores": risk_scores,
            "category_scores": result.category_scores,
            "repository_statistics": {
                "deployments": summary.total_deployments,
                "total_replicas": summary.total_replicas,
                "public_s3_buckets": summary.public_s3_buckets,
                "public_security_groups": summary.public_security_groups,
            },
            "findings": [vars(f) for f in result.findings],
            "recommendations": [vars(r) for r in result.recommendations],
            "ai_architecture_review": ai_architecture_review,
            "remediation_code": remediation_code,
            "benchmark_result": benchmark_result,
            "drift_result": drift_result,
            "cost_optimization": cost_result,
            "compliance_result": compliance_result,
            "recommendation_result": recommendation_result,
        }
