
from reportlab.platypus import (
Image,
Preformatted,
SimpleDocTemplate,
Paragraph,
Spacer,
PageBreak,
Table,
TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import (
ParagraphStyle,
getSampleStyleSheet
)

styles = getSampleStyleSheet()
code_style = ParagraphStyle(
    "Code",

    parent=styles["BodyText"],

    fontName="Courier",

    fontSize=7,

    leading=8,

    leftIndent=20,
)

class PdfReportService:

    def generate(
        self,
        report,
        output_file
    ):

        doc = SimpleDocTemplate(
            output_file
        )

        styles = getSampleStyleSheet()

        elements = []

        #
        # COVER PAGE
        #

        elements.append(
            Paragraph(
                "Architecture Review Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                f"Overall Score: "
                f"{report['overall_score']}",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Risk Level: "
                f"{report['risk_level']}",
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # EXECUTIVE SUMMARY
        #

        elements.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                report[
                    "narrative_summary"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # REPOSITORY STATISTICS
        #

        elements.append(
            Paragraph(
                "Repository Statistics",
                styles["Heading1"]
            )
        )

        stats = report[
            "repository_statistics"
        ]

        repo_data = [

            ["Metric", "Value"],

            [
                "Deployments",
                stats["deployments"]
            ],

            [
                "Total Replicas",
                stats["total_replicas"]
            ],

            [
                "Public S3 Buckets",
                stats[
                    "public_s3_buckets"
                ]
            ],

            [
                "Public Security Groups",
                stats[
                    "public_security_groups"
                ]
            ]
        ]

        repo_table = Table(
            repo_data,
            colWidths=[200, 100]
        )

        repo_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            repo_table
        )

        elements.append(
            PageBreak()
        )
        
        #
        # TOP RISKS
        #

        elements.append(
            Paragraph(
                "Top Risks",
                styles["Heading1"]
            )
        )

        for risk in report[
            "top_risks"
        ]:

            elements.append(
                Paragraph(
                    f"• {risk}",
                    styles["BodyText"]
                )
            )

        elements.append(
            Spacer(1, 20)
        )

        #
        # RECOMMENDATIONS
        #

        elements.append(
            Paragraph(
                "Recommendations",
                styles["Heading1"]
            )
        )

        for recommendation in report[
            "recommendations"
        ]:

            elements.append(
                Paragraph(
                    f"• {recommendation['message']}",
                    styles["BodyText"]
                )
            )
        
        elements.append(
            Spacer(1, 20)
        )
        #
        # ARCHITECTURE HEALTH ASSESSMENT
        #
        risk_scores = report[
            "risk_scores"
        ]
        
        elements.append(
            Paragraph(
                "Architecture Health Assessment",
                styles["Heading1"]
            )
        )

        health_data = [

            ["Metric", "Value"],

            [
                "Overall Score",
                f"{risk_scores['overall_score']}/100"
            ],

            [
                "Maturity Level",
                risk_scores[
                    "maturity_level"
                ]
            ],

            [
                "Risk Level",
                risk_scores[
                    "risk_level"
                ]
            ]
        ]

        health_table = Table(
            health_data,
            colWidths=[200, 200]
        )

        health_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            health_table
        )

        elements.append(
            Spacer(1, 20)
        )

        if (
            risk_scores["overall_score"]
            >= 80
        ):

            health_summary = (
                "The architecture follows most "
                "recommended cloud best practices."
            )

        elif (
            risk_scores["overall_score"]
            >= 60
        ):

            health_summary = (
                "The architecture contains moderate "
                "risks and improvement opportunities."
            )

        else:

            health_summary = (
                "The architecture contains significant "
                "security, reliability, or scalability risks."
            )
        
        elements.append(
            Paragraph(
                health_summary,
                styles["Italic"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # BENCHMARK RESULT
        #

        print(report["benchmark_result"])
        benchmark_result = report[
            "benchmark_result"
        ]

        elements.append(
            Paragraph(
                "Architecture Benchmarking",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Overall Benchmark Score: "
                f"{benchmark_result['overall_score']}%",
                styles["Heading2"]
            )
        )

        framework_data = [

            ["Framework", "Score"]
        ]

        for framework in benchmark_result[
            "frameworks"
        ]:

            framework_data.append(

                [
                    framework["name"],

                    f"{framework['score']}%"
                ]
            )
        
        framework_table = Table(
            framework_data,
            colWidths=[250, 100]
        )

        framework_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            framework_table
        )

        elements.append(
            Spacer(1, 20)
        )
        
        #
        # FAILED CONTROLS
        #

        elements.append(
            Paragraph(
                "Failed Controls",
                styles["Heading2"]
            )
        )

        for control in benchmark_result[
            "failed_controls"
        ]:

            elements.append(
                Paragraph(
                    f"• {control}",
                    styles["BodyText"]
                )
            )
        
        elements.append(
            Paragraph(
                "No failed controls detected.",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(
                1,
                20
            )
        )

        #
        # COMPLIANCE ASSESSMENT
        #

        compliance_result = report.get(
            "compliance_result",
            {
                "frameworks": []
            }
        )

        elements.append(
            Paragraph(
                "Compliance Assessment",
                styles["Heading1"]
            )
        )

        compliance_data = [

            ["Framework", "Score"]
        ]

        for framework in compliance_result[
            "frameworks"
        ]:

            compliance_data.append(

                [
                    framework["name"],

                    f"{framework['score']}%"
                ]
            )
        
        compliance_table = Table(
            compliance_data,
            colWidths=[250, 100]
        )

        compliance_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            compliance_table
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                "Failed Controls",
                styles["Heading2"]
            )
        )

        for framework in compliance_result[
            "frameworks"
        ]:

            elements.append(
                Paragraph(
                    framework["name"],
                    styles["Heading3"]
                )
            )

            if framework[
                "failed_controls"
            ]:

                for control in framework[
                    "failed_controls"
                ]:

                    elements.append(
                        Paragraph(
                            f"• {control}",
                            styles["BodyText"]
                        )
                    )

            else:

                elements.append(
                    Paragraph(
                        "No failed controls.",
                        styles["BodyText"]
                    )
                )

            elements.append(
                Spacer(
                    1,
                    10
                )
            )
        
        total_frameworks = len(
            compliance_result[
                "frameworks"
            ]
        )

        average_score = 0

        if total_frameworks > 0:

            average_score = int(

                sum(

                    framework["score"]

                    for framework in
                    compliance_result[
                        "frameworks"
                    ]
                )
                /
                total_frameworks
            )
        
        elements.append(
            Paragraph(
                f"Average Compliance Score: "
                f"{average_score}%",
                styles["Italic"]
            )
        )

        elements.append(
            Spacer(
                1,
                20
            )
        )

        #
        # DRIFT RESULTS
        #
        
        drift_result = report.get(
            "drift_result",
            {
                "drift_detected": False,
                "added_findings": [],
                "removed_findings": []
            }
        )

        elements.append(
            Paragraph(
                "Architecture Drift Analysis",
                styles["Heading1"]
            )
        )

        drift_data = [

            ["Metric", "Value"],

            [
                "Drift Detected",
                "Yes"
                if drift_result[
                    "drift_detected"
                ]
                else
                "No"
            ]
        ]

        drift_table = Table(
            drift_data,
            colWidths=[200, 150]
        )

        drift_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            drift_table
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                "New Findings",
                styles["Heading2"]
            )
        )

        if drift_result[
            "added_findings"
        ]:

            for finding in drift_result[
                "added_findings"
            ]:

                elements.append(
                    Paragraph(
                        f"• {finding}",
                        styles["BodyText"]
                    )
                )

        else:

            elements.append(
                Paragraph(
                    "No new findings detected.",
                    styles["BodyText"]
                )
            )
        
        elements.append(
            Paragraph(
                "Resolved Findings",
                styles["Heading2"]
            )
        )

        if drift_result[
            "removed_findings"
        ]:

            for finding in drift_result[
                "removed_findings"
            ]:

                elements.append(
                    Paragraph(
                        f"• {finding}",
                        styles["BodyText"]
                    )
                )

        else:

            elements.append(
                Paragraph(
                    "No findings were resolved.",
                    styles["BodyText"]
                )
            )
        
        if drift_result[
            "drift_detected"
        ]:

            summary = (
                "Architecture drift was detected "
                "between the previous and current "
                "assessment."
            )

        else:

            summary = (
                "No architecture drift was detected."
            )

        elements.append(
            Paragraph(
                summary,
                styles["Italic"]
            )
        )

        elements.append(
            Spacer(
                1,
                20
            )
        )

        #
        # COST OPTIMIZATION
        #

        cost_result = report.get(
            "cost_optimization",
            {
                "total_opportunities": 0,
                "opportunities": []
            }
        )

        elements.append(
            Paragraph(
                "Cost Optimization Opportunities",
                styles["Heading1"]
            )
        )

        cost_summary = [

            ["Metric", "Value"],

            [
                "Total Opportunities",
                str(
                    cost_result[
                        "total_opportunities"
                    ]
                )
            ]
        ]

        cost_table = Table(
            cost_summary,
            colWidths=[200, 150]
        )

        cost_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            cost_table
        )

        elements.append(
            Spacer(1, 20)
        )

        if not cost_result[
            "opportunities"
        ]:

            elements.append(
                Paragraph(
                    "No cost optimization opportunities detected.",
                    styles["BodyText"]
                )
            )
        else:
            for opportunity in cost_result[
                "opportunities"
            ]:

                elements.append(
                    Paragraph(
                        f"Finding: "
                        f"{opportunity['finding']}",
                        styles["Heading3"]
                    )
                )

                elements.append(
                    Paragraph(
                        f"Recommendation: "
                        f"{opportunity['recommendation']}",
                        styles["BodyText"]
                    )
                )

                elements.append(
                    Paragraph(
                        f"Impact: "
                        f"{opportunity['impact']}",
                        styles["BodyText"]
                    )
                )

        elements.append(
            Spacer(
                1,
                10
            )
        )

        #
        # ARCHITECTURE RECOMMENDATION
        #

        recommendation_result = report.get(
            "recommendation_result",
            {
                "target_architecture": "",
                "recommendations": [],
                "expected_improvements": {}
            }
        )

        elements.append(
            Paragraph(
                "Architecture Recommendations",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                "Target Architecture",
                styles["Heading2"]
            )
        )

        recommendation_text = (
            recommendation_result.get(
                "target_architecture",
                ""
            )
        )

        sections = (
            recommendation_text
            .split(
                "Top Recommendations:"
            )
        )

        target_architecture = (
            sections[0].strip()
        )

        recommendations = ""

        if len(sections) > 1:

            recommendations = (
                sections[1].strip()
            )

        #
        # Target Architecture
        #

        elements.append(
            Paragraph(
                target_architecture,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

        #
        # Recommendations
        #

        elements.append(
            Paragraph(
                "Recommended Improvements",
                styles["Heading2"]
            )
        )

        for line in recommendations.split("\n"):

            line = line.strip()

            if line:

                elements.append(
                    Paragraph(
                        line,
                        styles["BodyText"]
                    )
                )

        elements.append(
            Spacer(
                1,
                20
            )
        )

        #
        # ARCHITECTURE DOCUMENTATION
        #
        
        elements.append(
            Paragraph(
                "Architecture Documentation",
                styles["Heading1"]
            )
        )

        documentation = report[
            "architecture_documentation"
        ]

        #print("Architecture Documentation:")
        #print(report["architecture_documentation"])

        elements.append(
            Paragraph(
                "Overview",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                documentation[
                    "overview"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                "Traffic Flow",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                documentation[
                    "traffic_flow"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                "Scalability",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                documentation[
                    "scalability"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                "Security",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                documentation[
                    "security"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                "Operational Risks",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                documentation[
                    "operational_risks"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(
                1,
                10
            )
        )

        #
        # CATEGORY SCORE TABLE
        #

        elements.append(
            Paragraph(
                "Category Scores",
                styles["Heading1"]
            )
        )

        score_data = [

            ["Category", "Score"],

            [
                "Security",
                report["category_scores"][
                    "security"
                ]
            ],

            [
                "Availability",
                report["category_scores"][
                    "availability"
                ]
            ],

            [
                "Reliability",
                report["category_scores"][
                    "reliability"
                ]
            ],

            [
                "Scalability",
                report["category_scores"][
                    "scalability"
                ]
            ],

            [
                "Cost",
                report["category_scores"][
                    "cost"
                ]
            ],

            [
                "Observability",
                report["category_scores"][
                    "observability"
                ]
            ]
        ]

        score_table = Table(
            score_data,
            colWidths=[200, 100]
        )

        score_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            score_table
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # RISK BREAKDOWN TABLE
        #

        elements.append(
            Paragraph(
                "Risk Breakdown",
                styles["Heading1"]
            )
        )

        risk_breakdown = report[
            "dashboard"
        ][
            "risk_breakdown"
        ]

        risk_data = [

            ["Severity", "Count"],

            [
                "Critical",
                risk_breakdown[
                    "critical"
                ]
            ],

            [
                "High",
                risk_breakdown[
                    "high"
                ]
            ],

            [
                "Medium",
                risk_breakdown[
                    "medium"
                ]
            ],

            [
                "Low",
                risk_breakdown[
                    "low"
                ]
            ]
        ]

        risk_table = Table(
            risk_data,
            colWidths=[200, 100]
        )

        risk_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            risk_table
        )

        elements.append(
            Spacer(1, 20)
        )


        #
        # FINDINGS TABLE
        #

        elements.append(
            Paragraph(
                "Detailed Findings",
                styles["Heading1"]
            )
        )

        findings_data = [

            [
                "Severity",
                "Category",
                "Message"
            ]
        ]

        for finding in report[
            "findings"
        ]:

            findings_data.append([

                finding["severity"],

                finding["category"],

                finding["message"]
            ])

        findings_table = Table(
            findings_data,
            colWidths=[100, 120, 320]
        )

        findings_table.setStyle(
            TableStyle([

                ("GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black),

                ("BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey)
            ])
        )

        elements.append(
            findings_table
        )

        elements.append(
            PageBreak()
        )

        #
        # AI ARCHITECTURE REVIEW
        #

        elements.append(
            Paragraph(
                "AI Architecture Assessment",
                styles["Heading1"]
            )
        )

        ai_architecture_review = report[
            "ai_architecture_review"
        ]

        elements.append(
            Paragraph(
                "Executive Assessment",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                ai_architecture_review[
                    "executive_assessment"
                ],
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 15)
        )

        elements.append(
            Paragraph(
                "Top Priorities",
                styles["Heading2"]
            )
        )

        for priority in ai_architecture_review[
            "top_priorities"
        ]:

            elements.append(
                Paragraph(
                    f"• {priority}",
                    styles["BodyText"]
                )
            )

        elements.append(
            Spacer(1, 15)
        )

        elements.append(
            Paragraph(
                "Remediation Roadmap",
                styles["Heading2"]
            )
        )

        for step in ai_architecture_review[
            "remediation_roadmap"
        ]:

            elements.append(
                Paragraph(
                    f"Initiative: {step.get('name', '')}",
                    styles["Heading3"]
                )
            )

            elements.append(
                Paragraph(
                    step.get(
                        "description",
                        ""
                    ),
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    f"Timeline: {step.get('timeline', '')}",
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    "Implementation Steps:",
                    styles["BodyText"]
                )
            )

            for implementation_step in step.get(
                "steps",
                []
            ):

                elements.append(
                    Paragraph(
                        f"• {implementation_step}",
                        styles["BodyText"]
                    )
                )

            elements.append(
                Spacer(1, 10)
            )
        
        #
        # REMEDIATION CODE
        #
        elements.append(
            Paragraph(
                "Remediation Plan",
                styles["Heading1"]
            )
        )

        for item in report[
            "remediation_code"
        ][
            "remediations"
        ]:

            elements.append(
                Paragraph(
                    f"Finding: {item['finding']}",
                    styles["Heading3"]
                )
            )

            elements.append(
                Paragraph(
                    f"Priority: {item['priority']}",
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    f"Recommended Action: {item['remediation']}",
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    "Implementation Steps:",
                    styles["Heading4"]
                )
            )

            for step in item[
                "implementation_steps"
            ]:

                elements.append(
                    Paragraph(
                        f"• {step}",
                        styles["BodyText"]
                    )
                )

            elements.append(
                Spacer(
                    1,
                    10
                )
            )

        #
        # ARCHITECTURE DIAGRAM
        #
        '''
        elements.append(
            Paragraph(
                "Architecture Diagram",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                "Architecture Diagram",
                styles["Heading1"]
            )
        )

        elements.append(
            Image(
                report[
                    "architecture_diagram_image"
                ],
                width=450,
                height=250
            )
        )

        elements.append(
            Spacer(1, 20)
        )
        '''
        elements.append(
            Paragraph(
                "Architecture Diagram",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                "<pre>%s</pre>"
                %
                report[
                    "architecture_diagram"
                ].replace(
                    "\n",
                    "<br/>"
                ),
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        

        doc.build(
            elements
        )

        return output_file

