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

import {
  downloadPdf
} from "@/src/app/services/export";

import ChatAssistant
from "@/src/components/ui/ChatAssistant";

import ArchitectureDiagram
from "@/src/components/ui/ArchitectureDiagram";

import ArchitectureRedesign
from "@/src/components/ui/ArchitectureRedesign";

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

  async function
    handleExportPdf() {

    try {

        await downloadPdf(
        params.id as string
        );

    } catch (

        error

    ) {

        console.error(
        error
        );

        alert(
        "Failed to export PDF"
        );
    }
    }

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

        <div
        className="
            flex
            justify-between
            items-center
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

        <button

            onClick={
            handleExportPdf
            }

            className="
            bg-cyan-600
            hover:bg-cyan-700
            text-white
            px-4
            py-2
            rounded-lg
            transition
            "
        >

            Export PDF

        </button>

        </div>

        {
        report.findings && (

            <FindingsTable

                findings={
                    report.findings
                }

                reportId={
                    params.id as string
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
        <ChatAssistant

            reportId={
                params.id as string
            }

        />
        <ArchitectureDiagram

            reportId={
                params.id as string
            }

        />
        <ArchitectureRedesign

            reportId={
                params.id as string
            }

        />

    </main>

    );
}