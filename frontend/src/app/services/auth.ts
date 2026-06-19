import {
  API_URL
} from "@/src/lib/config";

const API_BASE =
  `${API_URL}/api/v1/auth`;

export async function
register(

  email: string,

  password: string

) {

  const response =
    await fetch(

      `${API_BASE}/register`,

      {
        method: "POST",

        headers: {

          "Content-Type":
          "application/json"
        },

        body: JSON.stringify({

          email,

          password
        })
      }
    );

  return await response.json();
}

export async function
login(

  email: string,

  password: string

) {

  const response =
    await fetch(

      `${API_BASE}/login`,

      {
        method: "POST",

        headers: {

          "Content-Type":
          "application/json"
        },

        body: JSON.stringify({

          email,

          password
        })
      }
    );

  return await response.json();
}