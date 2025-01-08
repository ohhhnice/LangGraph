from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import MessagesState
from graph import NewGraph

import sys
sys.path.append(".")
import os

from utils import get_config
for key, value in get_config("./apiconfig.yaml").items():
    os.environ[key] = value

graph = NewGraph(MessagesState)

messages = [AIMessage(content="So you said you were researching ocean mammals?", name="Bot"),
            HumanMessage(content="Yes, I know about whales. But what others should I learn about?", name="Lance")]

for m in messages:
    m.pretty_print()
    
output = graph.invoke({"messages": messages})

for m in output['messages']:
    m.pretty_print()