from langgraph.graph import END, StateGraph

from backend.app.langgraph.chief_architect_agent import architect_node
from backend.app.langgraph.reliability_agent import reliability_node
from backend.app.langgraph.review_state import ReviewState
from backend.app.langgraph.scalability_agent import scalability_node
from backend.app.langgraph.security_agent import security_node

graph = StateGraph(ReviewState)

graph.add_node("security", security_node)

graph.add_node("reliability", reliability_node)

graph.add_node("scalability", scalability_node)

graph.add_node("architect", architect_node)

graph.set_entry_point("security")

graph.add_edge("security", "reliability")

graph.add_edge("reliability", "scalability")

graph.add_edge("scalability", "architect")

graph.add_edge("architect", END)

review_graph = graph.compile()
