def scalability_node(
    state
):

    scalability_findings = [

        f

        for f
        in state["findings"]

        if f.category
        ==
        "scalability"
    ]

    state[
        "scalability_review"
    ] = (
        "\n".join(
            [
                f.message

                for f
                in scalability_findings
            ]
        )
    )

    return state