"use client";

import {
  useEffect,
  useRef,
  useState
} from "react";

import mermaid from "mermaid";

import {
  generateDiagram
} from "@/src/app/services/diagram";

interface Props {

  reportId: string;
}

export default function
ArchitectureDiagram({

  reportId

}: Props) {

  const [

    diagram,

    setDiagram

  ] = useState("");

  const [

    loading,

    setLoading

  ] = useState(false);

  const containerRef =
    useRef<HTMLDivElement>(
      null
    );

  async function
  handleGenerateDiagram() {

    try {

      setLoading(
        true
      );

      const result =

        await generateDiagram(

          reportId

        );

      setDiagram(

        result.diagram

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

  useEffect(() => {

    if (
      !diagram
    ) {

      return;
    }

    mermaid.initialize({

      startOnLoad:
        false

    });

    mermaid.render(

      "architecture-diagram",

      diagram

    )

    .then(

      (
        result
      ) => {

        if (
          containerRef.current
        ) {

          containerRef.current.innerHTML =
            result.svg;
        }

      }

    );

  }, [diagram]);

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
        Current Architecture
      </h2>

      <button

        onClick={
          handleGenerateDiagram
        }

        disabled={
          loading
        }

        className="
          bg-cyan-600
          hover:bg-cyan-700
          disabled:bg-slate-700
          text-white
          px-4
          py-2
          rounded-lg
        "
      >

        {

          loading

          ?

          "Generating..."

          :

          "Generate Current Architecture"

        }

      </button>

      {

        diagram && (

          <>

            <div

              ref={
                containerRef
              }

              className="
                mt-6
                bg-white
                p-4
                rounded
              "

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

                    {diagram}

                </pre>

                </details>
          </>

        )

      }

    </div>

  );
}