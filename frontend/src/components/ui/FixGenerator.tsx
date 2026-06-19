"use client";

import {
  useState
} from "react";

import {
  generateFix
} from "@/src/app/services/fix";

interface Props {

  reportId: string;

  finding: string;
}

export default function
FixGenerator({

  reportId,

  finding

}: Props) {

  const [

    fix,

    setFix

  ] = useState("");

  const [

    loading,

    setLoading

  ] = useState(false);

  async function
  handleGenerateFix() {

    try {

      setLoading(
        true
      );

      const result =

        await generateFix(

          reportId,

          finding

        );

      setFix(
        result.fix
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

  return (

    <div
      className="
        mt-4
      "
    >

      <button

        onClick={
          handleGenerateFix
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

          "Generate Fix"

        }

      </button>

      {

        fix && (

          <div
            className="
              mt-4
              bg-slate-900
              border
              border-slate-700
              rounded-lg
              p-4
              whitespace-pre-wrap
            "
          >

            {fix}

          </div>

        )

      }

    </div>

  );
}