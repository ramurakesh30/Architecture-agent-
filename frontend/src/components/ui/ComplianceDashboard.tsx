interface ComplianceFramework {

  name: string;

  score: number;

  passed_controls: number;

  total_controls: number;

  failed_controls: string[];
}

interface ComplianceDashboardProps {

  frameworks: ComplianceFramework[];
}

export default function ComplianceDashboard({
  frameworks
}: ComplianceDashboardProps) {

  return (

    <div
      className="
        bg-slate-900
        rounded-lg
        border
        border-slate-800
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
        Compliance Status
      </h2>

      <div
        className="
          space-y-6
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
                      bg-cyan-500
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
                        text-sm
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