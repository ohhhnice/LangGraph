from graph import newGraph
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage,AnyMessage
from langgraph.graph.message import add_messages

from langgraph.graph import MessagesState
    
config = {"configurable": {"thread_id": "1"}}

react_graph = newGraph(MessagesState, "gpt-4o")

# messages = [HumanMessage(content="Add 3 and 4.")]
# messages = react_graph.invoke({"messages": messages}, config)
# for m in messages['messages']:
#     m.pretty_print()
    
# messages = [HumanMessage(content="Multiply that by 2.")]
# messages = react_graph.invoke({"messages": messages}, config)
# for m in messages['messages']:
#     m.pretty_print()

messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 2. Divide the output by 5")]
messages = react_graph.invoke({"messages": messages}, config)
for m in messages['messages']:
    m.pretty_print()
