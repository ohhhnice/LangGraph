from langchain_openai import ChatOpenAI
import sys 
sys.path.append("./")
from demo.demo2.tools import multiply

def newAgentWithTools(model:str, tools:list):
    llm = ChatOpenAI(model = model)
    llm_with_tools = llm.bind_tools(tools)
    return llm_with_tools

def tool_calling_llm(state):
    return {"messages": [newAgentWithTools("gpt-4o", [multiply]).invoke(state["messages"])]}
    