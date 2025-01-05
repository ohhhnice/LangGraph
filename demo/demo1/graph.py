from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from func import *
from IPython.display import Image, display



def new_graph(State):
    builder = StateGraph(State)
    builder.add_node("node1", node1)
    builder.add_node("node2", node2)
    builder.add_node("node3", node3)

    builder.add_edge(START, "node1")
    builder.add_conditional_edges("node1", decide_mood)
    builder.add_edge("node2", END)
    builder.add_edge("node3", END)

    graph = builder.compile()

    mermaid_code = graph.get_graph().draw_mermaid_png()

    with open("./graph.jpg", "wb") as f:
        f.write(mermaid_code)

    return graph
