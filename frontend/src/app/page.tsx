"use client";
import { useEffect } from "react";

import { useRouter }
from "next/navigation";

import Link from "next/link";

export default function HomePage() {

  const router =
    useRouter();

  useEffect(() => {

    const token =

      localStorage.getItem(
        "token"
      );

    if (token) {

      router.replace(
        "/assessment"
      );

    } else {

      router.replace(
        "/login"
      );
    }

  }, [router]);

  return (

    <main
      className="
        flex
        flex-col
        justify-center
        items-center
        min-h-[85vh]
        px-8
      "
    >

      <div
        className="
          text-center
        "
      >

        <h1
          className="
            text-4xl
            font-bold
            text-cyan-400
            mb-4
          "
        >
          Architecture Agent
        </h1>

        <p
          className="
            text-slate-400
          "
        >
          Redirecting...
        </p>

      </div>

    </main>
  );
}