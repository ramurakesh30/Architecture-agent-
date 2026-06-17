import { authHeaders } from "@/src/lib/auth";

const API_BASE =
  "http://localhost:8000/api/v1";

export async function
getAssessmentHistory() {

  const response =
    await fetch(
      `${API_BASE}/reports`,
      {
        headers:
          authHeaders()
      }
    );

  if (
    !response.ok
  ) {

    throw new Error(
      "Failed to fetch assessment history"
    );
  }

  return await response.json();
}

export async function
getTrendData() {

  const response =
    await fetch(
      `${API_BASE}/reports/trends`,
      {
        headers:
          authHeaders()
      }
    );

  if (
    !response.ok
  ) {

    throw new Error(
      "Failed to fetch trend data"
    );
  }

  return await response.json();
}

export async function
getAssessmentReport(
  reportId: string
) {

  const response =
    await fetch(
      `http://localhost:8000/api/v1/reports/${reportId}`,
      {
        headers:
          authHeaders()
      }
    );

  if (
    !response.ok
  ) {

    throw new Error(
      "Failed to load assessment report"
    );
  }

  return await response.json();
}

export async function
compareReports(

  reportAId: string,

  reportBId: string

) {

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/compare?report_a_id=${reportAId}&report_b_id=${reportBId}`,

       {
        headers:
          authHeaders()
      }

    );

  return await response.json();
}