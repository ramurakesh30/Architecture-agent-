"use client";

import {
  useEffect,
  useState
} from "react";

import {
  useParams
} from "next/navigation";

import {
  getAssessmentReport
} from "@/src/app/services/history";

import FindingsTable from "@/src/components/ui/FindingsTable";

import ComplianceDashboard
from "@/src/components/ui/ComplianceDashboard";

import BenchmarkDashboard
from "@/src/components/ui/BenchmarkDashboard";

import RecommendationsDashboard
from "@/src/components/ui/RecommendationsDashboard";

export default function
AssessmentDetailsPage() {

  const params =
    useParams();

  const [
    report,
    setReport
  ] = useState<any>(
    null
  );

  const [
    loading,
    setLoading
  ] = useState(true);

  useEffect(() => {

    if (
      !params.id
    ) {
      return;
    }

    getAssessmentReport(
      params.id as string
    )

      .then(
        (
          data
        ) => {

          console.log(
            "ASSESSMENT REPORT",
            data
          );

          setReport(
            data
          );

          setLoading(
            false
          );
        }
      )

      .catch(
        (
          error
        ) => {

          console.error(
            error
          );

          setLoading(
            false
          );
        }
      );

  }, [params.id]);

  if (
    loading
  ) {

    return (

      <main
        className="
          p-8
        "
      >
        Loading...
      </main>
    );
  }

  if (
    !report
  ) {

    return (

      <main
        className="
          p-8
        "
      >
        Report not found
      </main>
    );
  }

  return (

    <main
      className="
        max-w-7xl
        mx-auto
        p-8
        space-y-8
      "
    >

      <h1
        className="
          text-4xl
          font-bold
        "
      >
        Assessment Details
      </h1>

      {
        report.findings && (

          <FindingsTable
            findings={
              report.findings
            }
          />

        )
      }

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

      {
        report.benchmark_result && (

          <BenchmarkDashboard

            overallScore={
                report.benchmark_result
                .overall_score
            }

            frameworks={
                report.benchmark_result
                .frameworks
            }

          />

        )
      }

      {
        report.recommendation_result &&
        report.recommendations && (

          <RecommendationsDashboard

            recommendationResult={
              report
              .recommendation_result
            }

            recommendations={
              report
              .recommendations
            }

          />

        )
      }

    </main>
  );
}