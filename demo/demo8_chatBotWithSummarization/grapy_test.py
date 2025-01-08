from graph import NewGraph
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage
from typing_extensions import TypedDict



import sys
sys.path.append(".")
import os

from utils import get_config
for key, value in get_config("./apiconfig.yaml").items():
    os.environ[key] = value
    
class State(MessagesState):
    summary: str
    
graph = NewGraph(State)


# Create a thread
config = {"configurable": {"thread_id": "1"}}

# Start conversation
input_message = HumanMessage(content="hi! I'm Lance")
output = graph.invoke({"messages": [input_message]}, config) 
    
input_message = HumanMessage(content="what's my name?")
output = graph.invoke({"messages": [input_message]}, config) 

input_message = HumanMessage(content="i like the 49ers!")
output = graph.invoke({"messages": [input_message]}, config) 

input_message = HumanMessage(content="i like Nick Bosa, isn't he the highest paid defensive player?")
output = graph.invoke({"messages": [input_message]}, config) 
for m in output['messages']:
    m.pretty_print()

