export function isLoggedIn() {

  if (
    typeof window ===
    "undefined"
  ) {

    return false;
  }

  return !!localStorage.getItem(
    "token"
  );
}

export function logout() {

  localStorage.removeItem(
    "token"
  );

  window.location.href =
    "/login";
}

export function
authHeaders() {

  const token =

    localStorage.getItem(
      "token"
    );

  return {

    Authorization:
    `Bearer ${token}`,

    "Content-Type":
    "application/json"
  };
}