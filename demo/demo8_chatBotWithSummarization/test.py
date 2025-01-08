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

config = {"configurable": {"thread_id": "1"}}
print(graph.get_state(config).values.get("summary",""))