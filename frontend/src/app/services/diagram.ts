import {
  authHeaders
} from "@/src/lib/auth";

export async function
generateDiagram(
  reportId: string
) {

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/${reportId}/diagram`,

      {

        method: "POST",

        headers:
          authHeaders()

      }

    );

  if (
    !response.ok
  ) {

    throw new Error(
      "Failed to generate diagram"
    );
  }

  return await response.json();
}