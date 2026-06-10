def security_node(
    state
):

    findings = state[
        "findings"
    ]

    security_findings = [

        f

        for f in findings

        if f.category
        ==
        "security"
    ]

    state[
        "security_review"
    ] = (
        "\n".join(
            [
                f.message

                for f
                in security_findings
            ]
        )
    )

    return state