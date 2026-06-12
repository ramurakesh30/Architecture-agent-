interface BenchmarkFramework {

  name: string;

  score: number;

  passed_controls: number;

  total_controls: number;

  failed_controls: string[];
}

interface BenchmarkDashboardProps {

  overallScore: number;

  frameworks: BenchmarkFramework[];
}

export default function BenchmarkDashboard({
  overallScore,
  frameworks
}: BenchmarkDashboardProps) {

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-lg
        p-6
        mt-8
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          mb-6
        "
      >
        Benchmark Status
      </h2>

      <div
        className="
          mb-8
        "
      >

        <div
          className="
            flex
            justify-between
            mb-2
          "
        >

          <span
            className="
              font-semibold
            "
          >
            Overall Benchmark Score
          </span>

          <span
            className="
              text-cyan-400
              font-bold
            "
          >
            {overallScore}%
          </span>

        </div>

        <div
          className="
            w-full
            bg-slate-800
            rounded-full
            h-4
          "
        >

          <div
            className="
              bg-cyan-500
              h-4
              rounded-full
            "
            style={{
              width:
                `${overallScore}%`
            }}
          />

        </div>

      </div>

      <div
        className="
          space-y-8
        "
      >

        {
          frameworks.map(
            (
              framework,
              index
            ) => (

              <div
                key={index}
              >

                <div
                  className="
                    flex
                    justify-between
                    mb-2
                  "
                >

                  <span
                    className="
                      font-semibold
                    "
                  >
                    {framework.name}
                  </span>

                  <span>
                    {framework.score}%
                  </span>

                </div>

                <div
                  className="
                    w-full
                    bg-slate-800
                    rounded-full
                    h-3
                  "
                >

                  <div
                    className="
                      bg-green-500
                      h-3
                      rounded-full
                    "
                    style={{
                      width:
                        `${framework.score}%`
                    }}
                  />

                </div>

                <div
                  className="
                    text-sm
                    text-slate-400
                    mt-2
                  "
                >

                  Passed:
                  {" "}
                  {framework.passed_controls}
                  {" / "}
                  {framework.total_controls}

                </div>

                {
                  framework.failed_controls.length > 0 && (

                    <div
                      className="
                        mt-3
                      "
                    >

                      <p
                        className="
                          text-red-400
                          mb-1
                        "
                      >
                        Failed Controls
                      </p>

                      <ul
                        className="
                          list-disc
                          ml-5
                          text-slate-300
                        "
                      >

                        {
                          framework.failed_controls.map(
                            (
                              control,
                              idx
                            ) => (

                              <li
                                key={idx}
                              >
                                {control}
                              </li>

                            )
                          )
                        }

                      </ul>

                    </div>

                  )
                }

              </div>

            )
          )
        }

      </div>

    </div>

  );
}