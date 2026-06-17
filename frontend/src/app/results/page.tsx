"use client";

import { useEffect, useState } from "react";

import { Report } from "@/src/types/report";

import FindingsTable from "@/src/components/ui/FindingsTable";

import ComplianceDashboard
from "@/src/components/ui/ComplianceDashboard";

import BenchmarkDashboard
from "@/src/components/ui/BenchmarkDashboard";

import RecommendationsDashboard
from "@/src/components/ui/RecommendationsDashboard";

export default function ResultsPage() {

  const [report, setReport] =
    useState<Report | null>(
      null
    );

  useEffect(() => {

    const data =
      sessionStorage.getItem(
        "report"
      );

    if (data) {

        const parsed =
        JSON.parse(data);

        console.log(
        "REPORT:",
        parsed
        );

        setReport(
        parsed
        );
    }

    

  }, []);

  if (!report) {

    return (

      <main className="p-8">

        <h1
          className="
            text-2xl
            font-bold
          "
        >
          Loading Results...
        </h1>

      </main>
    );
  }

  return (

    <main
      className="
        max-w-7xl
        mx-auto
        p-8
      "
    >

      <h1
        className="
          text-4xl
          font-bold
          mb-8
        "
      >
        Assessment Results
      </h1>

      {/* Category Scores */}

      <div
        className="
          grid
          grid-cols-1
          md:grid-cols-3
          gap-4
          mb-8
        "
      >

        <div
          className="
            bg-slate-900
            border
            border-slate-800
            rounded-lg
            p-6
          "
        >

          <h3
            className="
              text-slate-400
              mb-2
            "
          >
            Security
          </h3>

          <p
            className="
              text-4xl
              font-bold
              text-cyan-400
            "
          >
            {
              report?.category_scores
                ?.security ?? "-"
            }
          </p>

        </div>

        <div
          className="
            bg-slate-900
            border
            border-slate-800
            rounded-lg
            p-6
          "
        >

          <h3
            className="
              text-slate-400
              mb-2
            "
          >
            Reliability
          </h3>

          <p
            className="
              text-4xl
              font-bold
              text-cyan-400
            "
          >
            {
              report?.category_scores
                ?.reliability ?? "-"
            }
          </p>

        </div>

        <div
          className="
            bg-slate-900
            border
            border-slate-800
            rounded-lg
            p-6
          "
        >

          <h3
            className="
              text-slate-400
              mb-2
            "
          >
            Scalability
          </h3>

          <p
            className="
              text-4xl
              font-bold
              text-cyan-400
            "
          >
            {
              report?.category_scores
                ?.scalability ?? "-"
            }
          </p>

        </div>

      </div>

      {/* Findings */}

      <FindingsTable
        findings={
          report.findings
        }
      />

      {/* Compliance */}

      {
        report.compliance_result && (

          <ComplianceDashboard

            frameworks={
              report
                .compliance_result
                .frameworks
            }

          />

        )
      }

      {/* Benchmark */}
      
      {
        report.benchmark_result && (

            <BenchmarkDashboard

            overallScore={
                report
                .benchmark_result
                .overall_score
            }

            frameworks={
                report
                .benchmark_result
                .frameworks
            }

            />

        )
      }

      {/* Recommendation */}

      {
        report.recommendation_result &&
        report.recommendations && (

            <RecommendationsDashboard

             recommendationResult={
                report.recommendation_result
            }

            recommendations={
                report.recommendations
            }

            />

        )
      }

      {/* Architecture Documentation */}

      {
        report.architecture_documentation && (

          <div
            className="
              bg-slate-900
              border
              border-slate-800
              rounded-lg
              p-6
              mt-8
            "
          >

            <h2
              className="
                text-2xl
                font-bold
                mb-4
              "
            >
              Architecture Documentation
            </h2>

            <div
              className="
                space-y-6
              "
            >

              <div>

                <h3
                  className="
                    font-semibold
                    mb-2
                  "
                >
                  Overview
                </h3>

                <p>
                  {
                    report
                      .architecture_documentation
                      .overview
                  }
                </p>

              </div>

              <div>

                <h3
                  className="
                    font-semibold
                    mb-2
                  "
                >
                  Traffic Flow
                </h3>

                <p>
                  {
                    report
                      .architecture_documentation
                      .traffic_flow
                  }
                </p>

              </div>

              <div>

                <h3
                  className="
                    font-semibold
                    mb-2
                  "
                >
                  Scalability
                </h3>

                <p>
                  {
                    report
                      .architecture_documentation
                      .scalability
                  }
                </p>

              </div>

              <div>

                <h3
                  className="
                    font-semibold
                    mb-2
                  "
                >
                  Security
                </h3>

                <p>
                  {
                    report
                      .architecture_documentation
                      .security
                  }
                </p>

              </div>

              <div>

                <h3
                  className="
                    font-semibold
                    mb-2
                  "
                >
                  Operational Risks
                </h3>

                <p>
                  {
                    report
                      .architecture_documentation
                      .operational_risks
                  }
                </p>

              </div>

            </div>

          </div>

        )
      }

    </main>
  );
}