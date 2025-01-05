from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from agent import newAgentWithTools
from tools import *
from langgraph.checkpoint.memory import MemorySaver

def newGraph(state, model):
    mytools = [divide, multiply, add]
    assitent = newAgentWithTools(model, mytools)
    
    builder = StateGraph(state)

    builder.add_node("assistent", assitent)
    builder.add_node("tools", ToolNode(mytools))
    
    builder.add_edge(START, "assistent")
    builder.add_conditional_edges("assistent", tools_condition)
    builder.add_edge("tools", "assistent")

    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)
    
    mermaid_code = graph.get_graph().draw_mermaid_png()    
    with open("./demo/demo3/graph.jpg", "wb") as f:
        f.write(mermaid_code)
    
    return graph
    
