from langgraph.graph import StateGraph,START,END
from typing import Literal
import random
def node1(state):
    return {"value": [state["value"][-1] + 1]}

def node2(state):
    return {"value": [state["value"][-1] + 1]}

def node3(state):
   return {"value": [state["value"][-1] + 1]}


def newGraph(state, model="gpt-4o"):
    builder = StateGraph(state)
    builder.add_node("node1", node1)
    builder.add_node("node2", node2)
    # builder.add_node("node3", node3)
    
    builder.add_edge(START, "node1")
    builder.add_edge("node1", "node2")
    # builder.add_edge("node1", "node3")
    builder.add_edge("node2", END)
    # builder.add_edge("node3", END)
    graph = builder.compile()
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("./demo/demo4/graph.jpg", "wb") as f:
        f.write(mermaid_code)
        
    return graph
        