import { authHeaders } from "@/src/lib/auth";

export async function
downloadPdf(
  reportId: string
) {

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/${reportId}/pdf`,

      {
        method: "GET",

        headers:
          authHeaders()
      }

    );

  if (!response.ok) {

    throw new Error(
      "Failed to download PDF"
    );
  }

  const blob =
    await response.blob();

  const url =
    window.URL.createObjectURL(
      blob
    );

  const link =
    document.createElement(
      "a"
    );

  link.href = url;

  link.download =
    "architecture-report.pdf";

  document.body.appendChild(
    link
  );

  link.click();

  link.remove();

  window.URL.revokeObjectURL(
    url
  );
}