export async function
analyzeGithubRepository(
  repositoryUrl: string
) {

  const response =
    await fetch(

      "http://localhost:8000/api/v1/architecture/analyze-github",

      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json"
        },

        body: JSON.stringify({

          repository_url:
            repositoryUrl

        })
      }
    );

  return await response.json();
}