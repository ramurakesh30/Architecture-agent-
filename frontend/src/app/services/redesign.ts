import {
  authHeaders
} from "@/src/lib/auth";

export async function
generateRedesign(
  reportId: string
) {

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/${reportId}/redesign`,

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
      "Failed to generate redesign"
    );
  }

  return await response.json();
}