def reliability_node(state):

    reliability_findings = [f for f in state["findings"] if f.category == "reliability"]

    state["reliability_review"] = "\n".join([f.message for f in reliability_findings])

    return state
