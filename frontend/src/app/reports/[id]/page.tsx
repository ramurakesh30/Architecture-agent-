"use client";

import { useEffect } from "react";

import { useState } from "react";

import { useParams } from "next/navigation";

import RemediationPlan from
  "@/src/components/ui/RemediationPlan";

import {

  generateRemediationPlan

} from "@/src/app/services/remediation";

import { authHeaders } from "@/src/lib/auth";

export default function ReportDetailPage() {

  const params =
    useParams();

  const reportId =
    params.id as string;

  const [

    report,

    setReport

  ] = useState<any>(
    null
  );

  const [

    loading,

    setLoading

  ] = useState(
    true
  );

  const [

    remediation,

    setRemediation

  ] = useState<any>(
    null
  );

  const [

    loadingRemediation,

    setLoadingRemediation

  ] = useState(
    false
  );

  useEffect(() => {

    async function
    loadReport() {

      try {

        const response =
          await fetch(

            `http://localhost:8000/api/v1/reports/${reportId}`,

            {

              headers:
                authHeaders()

            }

          );

        if (
          !response.ok
        ) {

          throw new Error(
            "Failed to load report"
          );
        }

        const data =
          await response.json();

        setReport(
          data
        );

      } catch (

        error

      ) {

        console.error(
          error
        );

      } finally {

        setLoading(
          false
        );
      }
    }

    if (
      reportId
    ) {

      loadReport();
    }

  }, [reportId]);

  async function
  handleGenerateRemediation() {

    try {

      setLoadingRemediation(
        true
      );

      const result =

        await generateRemediationPlan(

          reportId

        );

      setRemediation(
        result
      );

    } catch (

      error

    ) {

      console.error(
        error
      );

    } finally {

      setLoadingRemediation(
        false
      );
    }
  }

  if (
    loading
  ) {

    return (

      <div
        className="
          p-8
          text-slate-300
        "
      >

        Loading report...

      </div>

    );
  }

  if (
    !report
  ) {

    return (

      <div
        className="
          p-8
          text-red-400
        "
      >

        Report not found.

      </div>

    );
  }

  return (

    <div
      className="
        max-w-6xl
        mx-auto
        p-8
        space-y-8
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

        <h1
          className="
            text-3xl
            font-bold
            text-cyan-400
            mb-4
          "
        >
          Assessment Report
        </h1>

        <p
          className="
            text-slate-300
          "
        >
          Repository:
          {" "}
          {
            report
            .repository_name
          }
        </p>

        <p
          className="
            text-slate-300
            mt-2
          "
        >
          Overall Score:
          {" "}
          {
            report
            .overall_score
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

        <h2
          className="
            text-2xl
            font-semibold
            text-cyan-400
            mb-4
          "
        >
          Findings
        </h2>

        {

          report.findings?.length > 0

          ?

          (

            <div
              className="
                space-y-4
              "
            >

              {

                report.findings.map(

                  (
                    finding: any,
                    index: number
                  ) => (

                    <div

                      key={index}

                      className="
                        border
                        border-slate-700
                        rounded
                        p-4
                      "
                    >

                      <p
                        className="
                          font-semibold
                        "
                      >
                        {
                          finding.title
                          ||
                          finding.rule
                          ||
                          "Finding"
                        }
                      </p>

                      <p
                        className="
                          text-slate-400
                          mt-2
                        "
                      >
                        {
                          finding.description
                          ||
                          finding.message
                        }
                      </p>

                    </div>

                  )

                )

              }

            </div>

          )

          :

          (

            <p
              className="
                text-slate-400
              "
            >
              No findings available.
            </p>

          )

        }

      </div>

      <button

        onClick={
          handleGenerateRemediation
        }

        disabled={
          loadingRemediation
        }

        className="
          bg-cyan-600
          hover:bg-cyan-700
          disabled:bg-slate-700
          text-white
          px-6
          py-3
          rounded-lg
          transition
        "
      >

        {

          loadingRemediation

          ?

          "Generating..."

          :

          "Generate Remediation Plan"

        }

      </button>

      {

        remediation &&

        (

          <RemediationPlan

            remediation={
              remediation
            }

          />

        )

      }

    </div>

  );
}