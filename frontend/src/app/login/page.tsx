"use client";

import { useState } from "react";

import {

  login

} from "@/src/app/services/auth";

export default function
LoginPage() {

  const [

    email,

    setEmail

  ] = useState("");

  const [

    password,

    setPassword

  ] = useState("");

  async function
  handleLogin() {

    const result =

      await login(

        email,

        password

      );

    localStorage.setItem(

      "token",

      result.access_token
    );

    window.location.href =
        "/";

    alert(
      "Logged in"
    );
  }

  return (

    <main
      className="
        max-w-md
        mx-auto
        p-8
      "
    >

      <h1
        className="
          text-3xl
          font-bold
          mb-4
        "
      >
        Login
      </h1>

      <input
        className="
          w-full
          p-3
          mb-3
          bg-slate-900
        "
        placeholder="Email"
        value={email}
        onChange={(e) =>
          setEmail(
            e.target.value
          )
        }
      />

      <input
        type="password"
        className="
          w-full
          p-3
          mb-3
          bg-slate-900
        "
        placeholder="Password"
        value={password}
        onChange={(e) =>
          setPassword(
            e.target.value
          )
        }
      />

      <button
        onClick={
          handleLogin
        }
        className="
            w-full
            bg-cyan-600
            hover:bg-cyan-700
            px-4
            py-3
            rounded-lg
            font-medium
            mt-4
        "
      >
        Login
      </button>

    </main>
  );
}