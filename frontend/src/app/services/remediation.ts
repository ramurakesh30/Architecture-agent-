import { authHeaders } from "@/src/lib/auth";

import {
  API_URL
} from "@/src/lib/config";

const API_BASE =
  `${API_URL}/api/v1`;

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