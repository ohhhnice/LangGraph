from langgraph.graph import StateGraph, START, END


def node1(state):
    if len(state["value"]) != 0:
        return {"value": [state["value"][-1]+1]}
    else:
        return {"value": [2]}

def NewGraph(state):
    builder = StateGraph(state)
    builder.add_node("node1", node1)
    builder.add_edge(START, "node1")
    builder.add_edge("node1", END)
    
    graph = builder.compile()
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("./demo/demo5_reducer/graph.jpg", "wb") as f:
        f.write(mermaid_code)
    return graph 

