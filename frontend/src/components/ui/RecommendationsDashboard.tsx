interface Recommendation {

  category: string;

  message: string;
}

export interface RecommendationResult {

    security: string;

    reliability: string;

    scalability: string;
  
}

interface RecommendationsDashboardProps {

  recommendationResult:
    RecommendationResult;

  recommendations:
    Recommendation[];
}

export default function RecommendationsDashboard({

  recommendationResult,

  recommendations

}: RecommendationsDashboardProps) {

  console.log(
    "recommendationResult",
    recommendationResult
  );  

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
        Architecture Recommendations
      </h2>

      {/* Expected Improvements */}

      <div
        className="
          mb-8
        "
      >

        <h3
          className="
            text-xl
            font-semibold
            mb-4
          "
        >
          Expected Improvements
        </h3>

        <div
          className="
            grid
            grid-cols-1
            md:grid-cols-3
            gap-4
          "
        >

          <div
            className="
              bg-slate-800
              p-4
              rounded-lg
            "
          >

            <p
              className="
                text-slate-400
              "
            >
              Security
            </p>

            <p
              className="
                text-2xl
                font-bold
                text-cyan-400
              "
            >
              {
                recommendationResult
                  .security
              }
            </p>

          </div>

          <div
            className="
              bg-slate-800
              p-4
              rounded-lg
            "
          >

            <p
              className="
                text-slate-400
              "
            >
              Reliability
            </p>

            <p
              className="
                text-2xl
                font-bold
                text-cyan-400
              "
            >
              {
                recommendationResult
                .reliability
              }
            </p>

          </div>

          <div
            className="
              bg-slate-800
              p-4
              rounded-lg
            "
          >

            <p
              className="
                text-slate-400
              "
            >
              Scalability
            </p>

            <p
              className="
                text-2xl
                font-bold
                text-cyan-400
              "
            >
              {
                recommendationResult
                .scalability
              }
            </p>

          </div>

        </div>

      </div>

      {/* Recommendations */}

      <div>

        <h3
          className="
            text-xl
            font-semibold
            mb-4
          "
        >
          Recommended Actions
        </h3>

        <div
          className="
            space-y-4
          "
        >

          {
            recommendations.map(

              (
                recommendation,
                index
              ) => (

                <div
                  key={index}
                  className="
                    bg-slate-800
                    rounded-lg
                    p-4
                    border
                    border-slate-700
                  "
                >

                  <div
                    className="
                      mb-3
                    "
                  >

                    <span
                      className="
                        px-3
                        py-1
                        rounded-full
                        text-sm
                        font-semibold
                        bg-cyan-500
                        text-white
                      "
                    >
                      {
                        recommendation
                          .category
                      }
                    </span>

                  </div>

                  <p
                    className="
                      text-white
                    "
                  >
                    {
                      recommendation
                        .message
                    }
                  </p>

                </div>

              )
            )
          }

        </div>

      </div>

    </div>
  );
}