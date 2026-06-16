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
            Array.isArray(reports) &&
            reports.map(

                (
                report
                ) => (

                <Link
                    key={report.id}
                    href={`/history/${report.id}`}
                >

                    <div
                    className="
                        bg-slate-900
                        border
                        border-slate-800
                        rounded-lg
                        p-5
                        hover:border-cyan-500
                        hover:scale-[1.01]
                        transition
                        cursor-pointer
                    "
                    >

                    <h3
                        className="
                        text-lg
                        font-semibold
                        mb-2
                        "
                    >
                        {
                        report
                            .repository_name
                        }
                    </h3>

                    <p
                        className="
                        text-cyan-400
                        font-medium
                        "
                    >
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
                        mt-2
                        "
                    >
                        {
                        formatDate(
                            report.created_at
                        )
                        }
                    </p>

                    </div>

                </Link>

                )
            )
            }

      </div>

    </main>
  );
}