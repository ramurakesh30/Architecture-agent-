"use client";

import {

  useEffect,

  useState

} from "react";

import { useRouter }
from "next/navigation";

import {

  getAssessmentHistory,

  compareReports

} from "@/src/app/services/history";

import ComparisonDashboard
from "@/src/components/ui/ComparisonDashboard";

export default function
ComparePage() {
  
  const router =
    useRouter();

  useEffect(() => {

    const token =

      localStorage.getItem(
        "token"
      );

    if (!token) {

      router.push(
        "/login"
      );
    }

  }, []);

  const [

    reports,

    setReports

  ] = useState<any[]>([]);

  const [

    reportA,

    setReportA

  ] = useState("");

  const [

    reportB,

    setReportB

  ] = useState("");

  const [

    comparison,

    setComparison

  ] = useState<any>(
    null
  );

  useEffect(() => {

    getAssessmentHistory()

      .then(
        setReports
      );

  }, []);

  async function
  runComparison() {

    const result =

      await compareReports(

        reportA,

        reportB

      );
    
    console.log(
        "COMPARE RESULT:",
        result
        );

    setComparison(
      result
    );
  }

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
        Compare Reports
      </h1>

      <div
        className="
          flex
          gap-4
          mb-8
        "
      >

        <select

          value={
            reportA
          }

          onChange={
            (
              e
            ) =>

              setReportA(
                e.target.value
              )
          }
          className="
            bg-slate-900
            text-white
            border
            border-slate-700
            rounded-lg
            px-4
            py-2
            focus:outline-none
            focus:ring-2
            focus:ring-cyan-500
            min-w-[300px]
          "
        >

          <option value="">
            Select Report A
          </option>

          {
            reports.map(

              (
                report
              ) => (

                <option

                  key={
                    report.id
                  }

                  value={
                    report.id
                  }
                >

                  {
                    report
                    .repository_name
                  }

                </option>
              )
            )
          }

        </select>

        <select

          value={
            reportB
          }

          onChange={
            (
              e
            ) =>

              setReportB(
                e.target.value
              )
          }
          className="
            bg-slate-900
            text-white
            border
            border-slate-700
            rounded-lg
            px-4
            py-2
            focus:outline-none
            focus:ring-2
            focus:ring-cyan-500
            min-w-[300px]
          "
        >

          <option value="">
            Select Report B
          </option>

          {
            reports.map(

              (
                report
              ) => (

                <option

                  key={
                    report.id
                  }

                  value={
                    report.id
                  }
                >

                  {
                    report
                    .repository_name
                  }

                </option>
              )
            )
          }

        </select>

        <button

          onClick={
            runComparison
          }

          className="
            bg-cyan-600
            px-4
            py-2
            rounded
          "
        >

          Compare

        </button>

      </div>

      {
        comparison && (

          <ComparisonDashboard

            comparison={
              comparison
            }

          />

        )
      }

    </main>
  );
}