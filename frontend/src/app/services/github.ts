import { authHeaders } from "@/src/lib/auth";

import {
  API_URL
} from "@/src/lib/config";

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

      `${API_URL}/api/v1/analyze-github`,

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