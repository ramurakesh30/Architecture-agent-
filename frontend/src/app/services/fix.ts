import {
  authHeaders
} from "@/src/lib/auth";

export async function
generateFix(

  reportId: string,

  finding: string

) {

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/${reportId}/fix`,

      {

        method: "POST",

        headers: {

          ...authHeaders(),

          "Content-Type":
            "application/json"

        },

        body: JSON.stringify({

          finding

        })

      }

    );

  if (
    !response.ok
  ) {

    throw new Error(
      "Failed to generate fix"
    );
  }

  return await response.json();
}