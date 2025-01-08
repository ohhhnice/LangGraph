import os
import sys
sys.path.append(".")

from utils.getParas import get_config

for key, value in get_config("apiconfig.yaml").items():
    os.environ[key] = value
    
    
from typing_extensions import TypedDict, Literal
from operator import add
from typing import Annotated
class TypedDictState(TypedDict):
    value: Annotated[list[int], "abc"]
    

from demo.demo4.graph import newGraph
from langgraph.graph.message import add_messages

# graph = newGraph(TypedDictState)
# value = graph.invoke({"value": [1]})
# print(value)

print(type(Annotated[int, '$', "abc"].__metadata__))

# def abc():
#     print(111)
    
# print(abc.__name__)
    