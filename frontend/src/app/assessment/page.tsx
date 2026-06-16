"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AssessmentPage() {

  const [file, setFile] =
    useState<File | null>(null);

  const [loading, setLoading] =
    useState(false);
  
  const [
    repositoryUrl,
    setRepositoryUrl
  ] = useState("");


  const router =
    useRouter();

  async function runAssessment() {

    if (!file) {

      alert(
        "Please select a ZIP file."
      );

      return;
    }


    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    try {

      setLoading(true);

      const response =
        await fetch(
          "http://localhost:8000/api/v1/architecture/analyze",
          {
            method: "POST",
            body: formData
          }
        );

      if (!response.ok) {

        throw new Error(
          "Assessment failed."
        );
      }

      const result =
        await response.json();

      sessionStorage.setItem(
        "report",
        JSON.stringify(
          result.report
        )
      );

      router.push(
        "/results"
      );

    } catch (error) {

      console.error(error);

      alert(
        "Assessment failed."
      );

    } finally {

      setLoading(false);
    }
  }

  async function runGithubAssessment() {

    if (
      !repositoryUrl.trim()
    ) {

      alert(
        "Please enter a GitHub repository URL"
      );

      return;
    }

    setLoading(true);

    try {

      const response =
        await fetch(

          "http://localhost:8000/api/v1/architecture/analyze-github",

          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

              repository_url:
                repositoryUrl

            })
          }
        );

      const report =
        await response.json();

      sessionStorage.setItem(

        "report",

        JSON.stringify(
          report
        )
      );

      router.push(
        "/results"
      );

    } catch (error) {

      console.error(
        error
      );

      alert(
        "GitHub analysis failed"
      );

    } finally {

      setLoading(false);
    }
  }

  return (

    <main
      className="
        flex
        justify-center
        items-center
        min-h-[85vh]
        px-4
      "
    >

      <div
        className="
          w-full
          max-w-2xl
          bg-slate-900
          border
          border-slate-800
          rounded-xl
          shadow-2xl
          p-10
        "
      >

        <h1
          className="
            text-3xl
            font-bold
            mb-3
          "
        >
          Architecture Assessment
        </h1>

        <p
          className="
            text-slate-400
            mb-8
          "
        >
          Upload a repository ZIP file containing
          Terraform, Kubernetes, AWS, Azure,
          or cloud infrastructure code.
        </p>

        <div
          className="
            border-2
            border-dashed
            border-slate-700
            rounded-lg
            p-8
            text-center
            mb-6
          "
        >

          <input

            type="file"

            accept=".zip"

            onChange={(event) => {

              const selected =
                event.target.files?.[0];

              if (selected) {

                setFile(
                  selected
                );
              }
            }}
          />

          {file && (

            <p
              className="
                mt-4
                text-cyan-400
              "
            >
              Selected File:
              {" "}
              {file.name}
            </p>

          )}

        </div>

        <button

          onClick={
            runAssessment
          }

          disabled={loading}

          className="
            w-full
            bg-cyan-500
            hover:bg-cyan-600
            disabled:bg-slate-600
            py-3
            rounded-lg
            font-semibold
            transition
          "
        >

          {
            loading
              ? "Running Assessment..."
              : "Run Assessment"
          }

        </button>

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
            mb-4
          "
        >
          Analyze GitHub Repository
        </h2>

        <input

          type="text"

          value={
            repositoryUrl
          }

          onChange={(e) =>

            setRepositoryUrl(
              e.target.value
            )

          }

          placeholder="
            https://github.com/org/repository
          "

          className="
            w-full
            p-3
            rounded
            bg-slate-800
            border
            border-slate-700
            mb-4
          "
        />

        <button

          onClick={
            runGithubAssessment
          }

          disabled={
            loading
          }

          className="
            bg-green-600
            hover:bg-green-700
            px-4
            py-2
            rounded
          "
        >

          {
            loading
              ? "Analyzing..."
              : "Analyze Repository"
          }

        </button>

      </div>

    </main>
  );
}