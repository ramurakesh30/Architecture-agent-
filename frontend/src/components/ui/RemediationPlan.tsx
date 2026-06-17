interface Recommendation {

  recommendation: string;

  effort: string;
}

interface RemediationPlanProps {

  remediation: {

    critical: Recommendation[];

    medium: Recommendation[];

    low: Recommendation[];
  };
}

export default function
RemediationPlan({

  remediation

}: RemediationPlanProps) {

  return (

    <div
      className="
        mt-8
        space-y-8
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          text-cyan-400
        "
      >
        Remediation Plan
      </h2>

      <SeveritySection

        title="Critical"

        items={
          remediation.critical
        }

      />

      <SeveritySection

        title="Medium"

        items={
          remediation.medium
        }

      />

      <SeveritySection

        title="Low"

        items={
          remediation.low
        }

      />

    </div>

  );
}

function SeveritySection({

  title,

  items

}: {

  title: string;

  items: {

    recommendation: string;

    effort: string;

  }[];

}) {

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-lg
        p-4
      "
    >

      <h3
        className="
          text-xl
          font-semibold
          mb-4
        "
      >
        {title}
      </h3>

      {

        items.length === 0 ?

        (

          <p
            className="
              text-slate-400
            "
          >
            No recommendations
          </p>

        )

        :

        (

          <div
            className="
              space-y-3
            "
          >

            {

              items.map(

                (
                  item,
                  index
                ) => (

                  <div

                    key={index}

                    className="
                      border
                      border-slate-700
                      rounded
                      p-3
                    "
                  >

                    <p>
                      {
                        item
                        .recommendation
                      }
                    </p>

                    <p
                      className="
                        text-sm
                        text-slate-400
                        mt-1
                      "
                    >
                      Effort:
                      {" "}
                      {
                        item
                        .effort
                      }
                    </p>

                  </div>

                )

              )

            }

          </div>

        )

      }

    </div>

  );
}