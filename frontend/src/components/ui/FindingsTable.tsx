interface Finding {

  message: string;
}

interface FindingsTableProps {

  findings: Finding[];
}


export default function FindingsTable({
  findings
}: FindingsTableProps) {

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
          mb-4
        "
      >
        Findings
      </h2>

      <table
        className="
          w-full
        "
      >

        <thead>

          <tr
            className="
              border-b
              border-slate-700
            "
          >

            <th
              className="
                text-left
                py-3
              "
            >
              Finding
            </th>

          </tr>

        </thead>

        <tbody>

          {
            (findings ?? []).map(
              (
                finding,
                index
              ) => (

                <tr
                  key={index}
                  className="
                    border-b
                    border-slate-800
                  "
                >

                  <td
                    className="
                      py-3
                    "
                  >
                    {finding.message}
                  </td>

                </tr>

              )
            )
          }

        </tbody>

      </table>

      <div
        className="
          mt-4
          text-sm
          text-slate-400
        "
      >

        Total Findings:
        {" "}
        {findings.length}

      </div>

    </div>

  );
}