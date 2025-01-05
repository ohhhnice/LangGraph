import sys
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
sys.path.append("./")


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

if __name__=="__main__":
    import os
    from utils import get_config
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
    from demo.demo2.graph import newGraph
    
    config_file_path = "apiconfig.yaml"
    for key, value in get_config(config_file_path).items():
        os.environ[key] = value
        
    graph = newGraph(State)
    messages = graph.invoke({"messages": HumanMessage(content="hello! My name is Lisa!")})
    for m in messages['messages']:
        m.pretty_print()
    
    messages = graph.invoke({"messages": HumanMessage(content="Tell me what is my name!")})
    for m in messages['messages']:
        m.pretty_print()
    
    
        
    