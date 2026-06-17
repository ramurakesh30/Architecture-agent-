import { authHeaders } from "@/src/lib/auth";

const API_BASE =
  "http://localhost:8000/api/v1";

export async function
generateRemediationPlan(
  reportId: string
) {

  const response =
    await fetch(

      `${API_BASE}/reports/${reportId}/remediation`,

      {

        method: "POST",

        headers:
          authHeaders()

      }

    );

  if (!response.ok) {

    throw new Error(
      "Failed to generate remediation plan"
    );
  }

  return await response.json();
}