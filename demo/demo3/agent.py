from langchain_openai import ChatOpenAI

def newAgentWithTools(model:str, tools:list):
    llm = ChatOpenAI(model = model)
    llm_with_tools = llm.bind_tools(tools)
    return lambda state: {"messages": [llm_with_tools.invoke(state["messages"])]}