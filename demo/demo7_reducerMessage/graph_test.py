from graph import NewGraph, NewGraphV2
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage



import sys
sys.path.append(".")
import os

from utils import get_config
for key, value in get_config("./apiconfig.yaml").items():
    os.environ[key] = value

messages = [AIMessage("Hi.", name="Bot", id="1")]
messages.append(HumanMessage("Hi.", name="Lance", id="2"))
messages.append(AIMessage("So you said you were researching ocean mammals?", name="Bot", id="3"))
messages.append(HumanMessage("Yes, I know about whales. But what others should I learn about?", name="Lance", id="4"))

# graph = NewGraph(MessagesState)
# output = graph.invoke({"messages": messages})
# for m in output["messages"]:
#     m.pretty_print()
    
graphV2 = NewGraphV2(MessagesState)
outputV2 = graphV2.invoke({"messages": messages})
for m in outputV2["messages"]:
    m.pretty_print()