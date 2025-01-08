from langchain_core.messages import RemoveMessage,trim_messages
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

llm = llm = ChatOpenAI(model="gpt-4o")

def filter_node(state):
    delete_message = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
    return {"messages": delete_message}

def chat_model_node(state):
    return {"messages": [llm.invoke(state["messages"])]}

def NewGraph(state):
    builder = StateGraph(state)
    builder.add_node("filter", filter_node)
    builder.add_node("chat_model", chat_model_node)
    
    builder.add_edge(START, "filter")
    builder.add_edge("filter","chat_model")
    builder.add_edge("chat_model", END)
    
    graph = builder.compile()
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("demo/demo7_reducerMessage/graph.jpg", "wb") as f:
        f.write(mermaid_code)
    return graph


def chat_model_node_v2(state):
    messages = trim_messages(messages = state["messages"], max_tokens=100, strategy="last",
            token_counter=ChatOpenAI(model="gpt-4o"),
            allow_partial=False)
    print("================")
    print(messages)
    print("================")
    return {"messages": [llm.invoke(messages)]}


def NewGraphV2(state):
    builder = StateGraph(state)
    builder.add_node("chat_model_V2", chat_model_node_v2)
    builder.add_edge(START, "chat_model_V2")
    builder.add_edge("chat_model_V2", END)
    
    graph = builder.compile()
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("demo/demo7_reducerMessage/graphV2.jpg", "wb") as f:
        f.write(mermaid_code)
    return graph