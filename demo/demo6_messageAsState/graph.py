from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")

def chat_model_node(state):
    return {"messages": llm.invoke(state["messages"])}


def NewGraph(MessagesState):
    builder = StateGraph(MessagesState)
    builder.add_node("chat model", chat_model_node)
    builder.add_edge(START, "chat model")
    builder.add_edge("chat model", END)
    
    graph = builder.compile()
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("demo/demo6_messageAsState/graph.jpg", "wb") as f:
        f.write(mermaid_code)
        
    return graph