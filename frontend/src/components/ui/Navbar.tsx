import Link from "next/link";

export default function Navbar() {

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
            text-slate-300
          "
        >

          <Link
            href="/"
            className="
              hover:text-cyan-400
            "
          >
            Dashboard
          </Link>

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
            href="/results"
            className="
              hover:text-cyan-400
            "
          >
            Results
          </Link>

        </div>

      </div>

    </nav>
  );
}