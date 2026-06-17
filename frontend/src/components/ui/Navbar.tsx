"use client";

import Link from "next/link";

import {
  useEffect,
  useState
} from "react";

import {

  isLoggedIn,

  logout

} from "@/src/lib/auth";

export default function Navbar() {

  const [loggedIn, setLoggedIn] =
    useState(false);

  const [mounted, setMounted] =
    useState(false);

  useEffect(() => {

    setMounted(true);

    setLoggedIn(
      !!localStorage.getItem(
        "token"
      )
    );

  }, []);

  const handleLogout = () => {

    localStorage.removeItem(
      "token"
    );

    window.location.href =
      "/login";
  };

  if (!mounted) {

    return null;
  }

  return (

    <nav
      className="
        border-b
        border-slate-800
        bg-slate-900/80
        backdrop-blur
        px-8
        py-4
      "
    >

      <div
        className="
          max-w-7xl
          mx-auto
          flex
          justify-between
          items-center
        "
      >

        <Link
          href="/"
          className="
            text-xl
            font-bold
            text-cyan-400
          "
        >
          Architecture Agent
        </Link>

        <div
          className="
            flex
            gap-6
            items-center
            text-slate-300
          "
        >

          {
            loggedIn ?

            <>

              <Link
                href="/assessment"
                className="
                  hover:text-cyan-400
                "
              >
                Assessment
              </Link>

              <Link
                href="/history"
                className="
                  hover:text-cyan-400
                "
              >
                History
              </Link>

              <Link
                href="/trends"
                className="
                  hover:text-cyan-400
                "
              >
                Trends
              </Link>

              <Link
                href="/compare"
                className="
                  hover:text-cyan-400
                "
              >
                Compare
              </Link>

              <button

                onClick={
                  handleLogout
                }

                className="
                  bg-cyan-600
                  hover:bg-cyan-700
                  text-white
                  px-4
                  py-2
                  rounded-lg
                  transition
                "
              >

                Logout

              </button>

            </>

            :

            <>

              <Link
                href="/login"
                className="
                  px-4
                  py-2
                  rounded-lg
                  border
                  border-cyan-500
                  text-cyan-400
                  hover:bg-cyan-500
                  hover:text-white  
                  transition
                "
              >
                Login
              </Link>

              <Link
                href="/register"
                className="
                  px-4
                  py-2
                  rounded-lg
                  bg-cyan-600
                  text-white
                  hover:bg-cyan-700
                  transition
                "
              >
                Register
              </Link>

            </>

          }

        </div>

      </div>

    </nav>
  );
}