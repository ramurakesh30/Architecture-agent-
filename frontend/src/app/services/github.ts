import { authHeaders } from "@/src/lib/auth";

export async function
analyzeGithubRepository(
  repositoryUrl: string) 
{
  
  console.log(
   "TOKEN:",
   localStorage.getItem("token")
  );
  const response =
    await fetch(

      "http://localhost:8000/api/v1/analyze-github",

      {
        method: "POST",

        headers: {
            "Content-Type": "application/json",

            Authorization:
            `Bearer ${localStorage.getItem("token")}`
        },


        body: JSON.stringify({

          repository_url:
            repositoryUrl

        })
      }
    );

  return await response.json();
}