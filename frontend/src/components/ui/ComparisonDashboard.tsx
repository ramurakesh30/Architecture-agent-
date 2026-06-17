interface ComparisonDashboardProps {

  comparison: any;
}

export default function
ComparisonDashboard({

  comparison

}: ComparisonDashboardProps) {

  const reportA =
    comparison.report_a;

  const reportB =
    comparison.report_b;

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-lg
        p-6
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          mb-6
        "
      >
        Comparison Results
      </h2>

      <table
        className="
          w-full
        "
      >

        <thead>

          <tr>

            <th>
              Metric
            </th>

            <th>
              Report A
            </th>

            <th>
              Report B
            </th>

          </tr>

        </thead>

        <tbody>

          <tr>

            <td>
              Overall Score
            </td>

            <td>
              {
                reportA
                  .overall_score
              }
            </td>

            <td>
              {
                reportB
                  .overall_score
              }
            </td>

          </tr>

          <tr>

            <td>
              Security
            </td>

            <td>
              {
                reportA
                .category_scores
                .security
              }
            </td>

            <td>
              {
                reportB
                .category_scores
                .security
              }
            </td>

          </tr>

          <tr>

            <td>
              Reliability
            </td>

            <td>
              {
                reportA
                .category_scores
                .reliability
              }
            </td>

            <td>
              {
                reportB
                .category_scores
                .reliability
              }
            </td>

          </tr>

          <tr>

            <td>
              Scalability
            </td>

            <td>
              {
                reportA
                .category_scores
                .scalability
              }
            </td>

            <td>
              {
                reportB
                .category_scores
                .scalability
              }
            </td>

          </tr>

        </tbody>

      </table>

    </div>

  );
}