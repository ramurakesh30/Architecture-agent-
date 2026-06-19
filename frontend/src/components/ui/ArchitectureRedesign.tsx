"use client";

import {
  useState
} from "react";

import {
  generateRedesign
} from "@/src/app/services/redesign";

import MermaidRenderer
from "@/src/components/ui/MermaidRenderer";

interface Props {

  reportId: string;
}

export default function
ArchitectureRedesign({

  reportId

}: Props) {

  const [

    redesign,

    setRedesign

  ] = useState<any>(
    null
  );

  const [

    loading,

    setLoading

  ] = useState(
    false
  );

  async function
  handleGenerate() {

    try {

      setLoading(
        true
      );

      const result =

        await generateRedesign(
          reportId
        );

      setRedesign(
        result
      );

    } catch (

      error

    ) {

      console.error(
        error
      );

      alert(
        "Failed to generate redesign"
      );

    } finally {

      setLoading(
        false
      );
    }
  }

  return (

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
        Architecture Refactoring Advisor
      </h2>

      <button

        onClick={
          handleGenerate
        }

        disabled={
          loading
        }

        className="
          bg-cyan-600
          hover:bg-cyan-700
          disabled:bg-slate-700
          px-4
          py-2
          rounded-lg
          text-white
        "
      >

        {

          loading

          ?

          "Generating..."

          :

          "Generate Target Architecture"

        }

      </button>

      {

        redesign && (

          <div
            className="
              mt-6
              space-y-8
            "
          >

            <div>

              <h3
                className="
                  text-xl
                  font-bold
                  mb-2
                "
              >
                Current Problems
              </h3>

              <div
                className="
                  bg-slate-800
                  rounded-lg
                  p-4
                  whitespace-pre-wrap
                "
              >
                {
                  redesign.current_problems
                }
              </div>

            </div>

            <div>

              <h3
                className="
                  text-xl
                  font-bold
                  mb-2
                "
              >
                Target Architecture
              </h3>

              <div
                className="
                  bg-slate-800
                  rounded-lg
                  p-4
                  whitespace-pre-wrap
                "
              >
                {
                  redesign.target_architecture
                }
              </div>

            </div>

            <div>

              <h3
                className="
                  text-xl
                  font-bold
                  mb-2
                "
              >
                Migration Plan
              </h3>

              <div
                className="
                  bg-slate-800
                  rounded-lg
                  p-4
                  whitespace-pre-wrap
                "
              >
                {
                  redesign.migration_plan
                }
              </div>

            </div>

            {

              redesign.scorecard && (

                <div>

                  <h3
                    className="
                      text-xl
                      font-bold
                      mb-2
                    "
                  >
                    Architecture Scorecard
                  </h3>

                  <div
                    className="
                      grid
                      grid-cols-2
                      gap-4
                    "
                  >

                    <div
                      className="
                        bg-slate-800
                        rounded-lg
                        p-4
                      "
                    >
                      Security:
                      {" "}
                      {
                        redesign
                        .scorecard
                        .security
                      }
                      /10
                    </div>

                    <div
                      className="
                        bg-slate-800
                        rounded-lg
                        p-4
                      "
                    >
                      Scalability:
                      {" "}
                      {
                        redesign
                        .scorecard
                        .scalability
                      }
                      /10
                    </div>

                    <div
                      className="
                        bg-slate-800
                        rounded-lg
                        p-4
                      "
                    >
                      Reliability:
                      {" "}
                      {
                        redesign
                        .scorecard
                        .reliability
                      }
                      /10
                    </div>

                    <div
                      className="
                        bg-slate-800
                        rounded-lg
                        p-4
                      "
                    >
                      Cost:
                      {" "}
                      {
                        redesign
                        .scorecard
                        .cost
                      }
                      /10
                    </div>

                  </div>

                </div>

              )

            }

            {

              redesign.diagram && (

                <div>

                  <h3
                    className="
                      text-xl
                      font-bold
                      mb-4
                    "
                  >
                    Target Architecture Diagram
                  </h3>

                  <MermaidRenderer

                    diagram={
                      redesign.diagram
                    }

                  />

                  <details
                    className="
                      mt-4
                    "
                  >

                    <summary
                      className="
                        cursor-pointer
                        text-cyan-400
                      "
                    >
                      Show Mermaid Source
                    </summary>

                    <pre
                      className="
                        mt-2
                        bg-slate-950
                        rounded-lg
                        p-4
                        overflow-auto
                        text-sm
                      "
                    >

                      {
                        redesign.diagram
                      }

                    </pre>

                  </details>

                </div>

              )

            }

          </div>

        )

      }

    </div>

  );
}