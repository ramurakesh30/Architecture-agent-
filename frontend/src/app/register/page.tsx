"use client";

import { useState } from "react";

import {

  register

} from "@/src/app/services/auth";

export default function
RegisterPage() {

  const [

    email,

    setEmail

  ] = useState("");

  const [

    password,

    setPassword

  ] = useState("");

  async function
  handleRegister() {

    await register(

      email,

      password

    );

    alert(
      "Registered"
    );
    window.location.href =
        "/login";
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
        Register
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
          handleRegister
        }
        className="
            w-full
            bg-green-600
            hover:bg-green-700
            px-4
            py-3
            rounded-lg
            font-medium
            mt-4
        "
      >
        Register
      </button>

    </main>
  );
}