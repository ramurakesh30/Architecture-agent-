from reportlab.platypus import (
Image,
SimpleDocTemplate,
Paragraph,
Spacer,
PageBreak,
Table,
TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import (
getSampleStyleSheet
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
        #
        # AI ARCHITECTURE REVIEW
        #

        elements.append(
            Paragraph(
                "AI Architecture Assessment",
                styles["Heading1"]
            )
        )

        ai_review = report[
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
                ai_review[
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

        for priority in ai_review[
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

        for step in ai_review[
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

        print("Architecture Documentation:")
        print(report["architecture_documentation"])

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

        doc.build(
            elements
        )

        return output_file

