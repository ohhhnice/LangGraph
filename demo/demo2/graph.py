import sys
sys.path.append("./")

from langgraph.graph import StateGraph, START, END
from demo.demo2.tools import multiply
from demo.demo2.agents import tool_calling_llm


def newGraph(state):
    builder = StateGraph(state)
    
    builder.add_node("llm_with_tools", tool_calling_llm)
    
    builder.add_edge(START, "llm_with_tools")
    builder.add_edge("llm_with_tools", END)
    
    graph = builder.compile()
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("./demo/demo2/graph1.jpg", "wb") as f:
        f.write(mermaid_code)
    return graph
        
    