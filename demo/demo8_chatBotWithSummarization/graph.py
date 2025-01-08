from langgraph.graph import StateGraph,START, END
from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
model = ChatOpenAI(model="gpt-4o",temperature=0)
import sqlite3

# memory = MemorySaver()

def NewGraph(state):
    builder = StateGraph(state)
    builder.add_node("conversation", conversation_node)
    builder.add_node("summarize_conversation", summarize_node)
    
    builder.add_edge(START, "conversation")
    builder.add_conditional_edges("conversation", continue_node)
    builder.add_edge("summarize_conversation", END)
    
    dbPath = "./demo/demo8_chatBotWithSummarization/snapeshot.db"
    conn = sqlite3.connect(dbPath, check_same_thread=False)
    memory = SqliteSaver(conn)
    
    graph = builder.compile(checkpointer=memory)
    
    mermaid_code = graph.get_graph().draw_mermaid_png()
    with open("./demo/demo8_chatBotWithSummarization/graph.jpg", "wb") as f:
        f.write(mermaid_code)
    return graph


def conversation_node(state):
    summary = state.get("summary","")
    
    if summary:
        system_messages = f"Summary of conversation earlier: {summary}"
        messages = [SystemMessage(content=system_messages)] + state["messages"]
    else:
        messages = state["messages"]
        
    response = model.invoke(messages)
    return {"messages": response}

def summarize_node(state):
    summary = state.get("summary", "")
    if summary:
        summary_message = (
            f"This is summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above:"
        )
    else:
        summary_message = "Create a summary of the conversation above:"
        
    messages = state["messages"] + [HumanMessage(content=summary_message)]
    response = model.invoke(messages)
    delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
    
    return {"summary": response.content, "messages": delete_messages}
    

def continue_node(state):
    if len(state["messages"])>6:
        return "summarize_conversation"
    return END
