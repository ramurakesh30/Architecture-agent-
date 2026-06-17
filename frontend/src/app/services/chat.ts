import {
  authHeaders
} from "@/src/lib/auth";

export async function
askReportQuestion(

  reportId: string,

  question: string

) {
  console.log(
    "Sending question:",
    question
  );

  const response =
    await fetch(

      `http://localhost:8000/api/v1/reports/${reportId}/chat`,

      {

        method: "POST",

        headers: {

          ...authHeaders(),

          "Content-Type":
            "application/json"

        },

        body: JSON.stringify({

          question

        })

      }

    );
    console.log(
        "Status:",
        response.status
    );

  const data =
    await response.json();

  console.log(
    "Response:",
    data
  );

  return data;
}