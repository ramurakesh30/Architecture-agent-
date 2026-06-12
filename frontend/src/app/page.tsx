import Link from "next/link";

export default function HomePage() {

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
          max-w-4xl
          text-center
        "
      >

        <h1
          className="
            text-6xl
            font-bold
            mb-6
            text-cyan-400
          "
        >
          Architecture Agent
        </h1>

        <p
          className="
            text-xl
            text-slate-300
            mb-10
          "
        >
          AI-powered cloud architecture review,
          compliance validation,
          benchmarking,
          remediation generation,
          and architecture recommendations.
        </p>

        <Link
          href="/assessment"
          className="
            inline-block
            bg-cyan-500
            hover:bg-cyan-600
            px-8
            py-4
            rounded-lg
            font-semibold
            text-lg
            transition
          "
        >
          Start Assessment
        </Link>

      </div>

    </main>
  );
}