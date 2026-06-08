from app.agents.kubernetes_agent import KubernetesAgent
from app.agents.terraform_agent import TerraformAgent
from app.agents.infrastructure_agent import InfrastructureAgent

from app.parsers.kubernetes_parser import KubernetesParser
from app.parsers.terraform_parser import TerraformParser

from app.domain.infrastructure import InfrastructurePackage
from app.domain.review_results import ReviewResult

from app.agents.architecture_insight_agent import (
    ArchitectureInsightAgent
)

from backend.services.dashboard_service import DashboardService

from backend.services.diagram_renderer_service import DiagramRendererService

from backend.services.finding_correlation_service import (
    FindingCorrelationService
)
from backend.services.infrastructure_aggregator import (
    InfrastructureAggregator
)
from backend.services.executive_summary_service import (
    ExecutiveSummaryService
)

from backend.services.architecture_diagram_service import (
    ArchitectureDiagramService
)

from backend.services.architecture_documentation_service import (
    ArchitectureDocumentationService
)
from backend.services.narrative_summary_service import (
    NarrativeSummaryService
)

from backend.services.dashboard_service import (
    DashboardService
)

from backend.services.ai_review_service import (
    AIReviewService
)

from app.providers.provider_factory import (
    ProviderFactory
)

class ArchitectureReviewService:

    def __init__(self):

        self.kubernetes_parser = KubernetesParser()

        self.terraform_parser = TerraformParser()

        self.kubernetes_agent = KubernetesAgent()

        self.terraform_agent = TerraformAgent()

        self.infrastructure_agent = InfrastructureAgent()

        self.aggregator = (
            InfrastructureAggregator()
        )

        self.insight_agent = (
            ArchitectureInsightAgent()
        )

        self.correlation_service = (
            FindingCorrelationService()
        )

        self.executive_summary_service = (
            ExecutiveSummaryService()
        )

        self.diagram_service = (
            ArchitectureDiagramService()
        )

        self.diagram_renderer_service = (
            DiagramRendererService()
        )

        self.narrative_summary_service = (
            NarrativeSummaryService()
        )


        self.dashboard_service = (
            DashboardService()
       )
        
        provider = (
            ProviderFactory.create()
        )

        self.ai_review_service = (
            AIReviewService(provider)
        )

        self.architecture_documentation_service = (
            ArchitectureDocumentationService(self.ai_review_service)
        )
    
    def analyze(
        self,
        files
    ):

        package = InfrastructurePackage()

        for file in files:

            with open(file, "r", encoding="utf-8") as f:

                content = f.read()

            if file.endswith((".yaml", ".yml")):

              package.kubernetes_configs.append(
                self.kubernetes_parser.parse(
                  content
                )
              )

            elif file.endswith(".tf"):

                package.terraform_configs.append(
                    self.terraform_parser.parse(
                        content
                    )
                )

        result = ReviewResult()

        for k8s in package.kubernetes_configs:

            self.kubernetes_agent.analyze(
                k8s,
                result
            )

        for tf in package.terraform_configs:

            self.terraform_agent.analyze(
                tf,
                result
            )
        summary = self.aggregator.summarize(
            package
        )

        self.infrastructure_agent.analyze(
            package,
            summary,
            result
        )
        self.insight_agent.analyze(
            summary,
            result
     )
        result = self.correlation_service.deduplicate(result)
        
        result.calculate_overall_score()

        findings = [

            f.message

            for f in result.findings
        ]

        ai_architecture_review = (
            self.ai_review_service
            .generate_architecture_review(
                findings
            )
        )

        summary_report = (
            self.executive_summary_service.generate(
                result
            )
        )

        diagram = (
            self.diagram_service.generate(
                summary
            )
        )

       # diagram_image = (
       #     self.diagram_renderer_service
       #     .render(
       #         diagram,
       #        "architecture.png"
        #    )
        #)

        architecture_documentation = (
            self.architecture_documentation_service
            .generate(
                summary
            )
        )

        narrative_summary = (
            self.narrative_summary_service.generate(
                result
            )
        )

        dashboard = ( 
            self.dashboard_service.build(
                { 
                    "overall_score":
                    result.overall_score,
                    "risk_level":
                        summary_report[ "risk_level" ],
                    "category_scores":
                        result.category_scores,
                    "top_risks": summary_report[ "top_risks" ],
                    "narrative_summary": narrative_summary,
                    "findings": [
                        vars(f)
                        for f in result.findings
                    ]
                }
            )
        )

        return {
            "overall_score":
                result.overall_score,

            "risk_level":
                summary_report["risk_level"],

            "executive_summary":
                summary_report["executive_summary"],
            
            "architecture_diagram":
                diagram,
            
           # "architecture_diagram_image":
           # diagram_image,
            
            "architecture_documentation":
                architecture_documentation,
            
            "narrative_summary":
                narrative_summary,

            "top_risks":
                summary_report["top_risks"],

            "category_summary":
                summary_report["category_summary"],
            
            "dashboard": dashboard,

            "category_scores":
                result.category_scores,
            
            "repository_statistics": { 
                "deployments":
                  summary.total_deployments,
                
                "total_replicas":
                  summary.total_replicas,
                
                "public_s3_buckets":
                  summary.public_s3_buckets,
                
                "public_security_groups":
                  summary.public_security_groups
                },

            "findings":
                [vars(f) for f in result.findings],

            "recommendations":
                [vars(r) for r in result.recommendations],
            
            "ai_architecture_review":
                ai_architecture_review

        }