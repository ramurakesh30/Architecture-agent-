"use client";

import {
  useEffect,
  useState
} from "react";

import Link from "next/link";

import {
  getAssessmentHistory
} from "@/src/app/services/history";

function formatDate(
  dateString: string
) {

  return new Date(
    dateString
  ).toLocaleString(
    "en-US",
    {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit"
    }
  );
}

export default function
HistoryPage() {

  const [
    reports,
    setReports
  ] = useState<any[]>([]);

  useEffect(() => {

    getAssessmentHistory()

      .then((data) => {

        console.log(
            "REPORTS:",
            data
        );

        console.log(
            "IS ARRAY:",
            Array.isArray(data)
        );

        setReports(
            Array.isArray(data)
            ? data
            : data.reports || []
        );

        });

  }, []);

  return (

    <main
      className="
        max-w-6xl
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
        Assessment History
      </h1>

      <div
        className="
          space-y-4
        "
      >

        {
          reports.map(
            (
              report
            ) => (

              <div
                key={
                  report.id
                }
                className="
                  bg-slate-900
                  border
                  border-slate-800
                  rounded-lg
                  p-4
                "
              >

                <h3
                  className="
                    text-lg
                    font-semibold
                  "
                >
                  {
                    report
                    .repository_name
                  }
                </h3>

                <p>
                  Score:
                  {" "}
                  {
                    report
                    .overall_score
                  }
                </p>

                <p
                    className="
                        text-slate-400
                        text-sm
                    "
                >
                    {formatDate(report.created_at)}
                </p>

              </div>

            )
          )
        }

      </div>

    </main>
  );
}