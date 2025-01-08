import sys
import os
sys.path.append(".")

from utils import get_config
for key, value in get_config("./apiconfig.yaml").items():
    os.environ[key] = value
    
    
from demo.demo5_reducer.graph import NewGraph

from typing import TypedDict, Annotated
from operator import add

def NodeReducer(left:list[int] | None, right:list[int] | None) -> list[int]:
    if not left:
        left = []
    if not right:
        right = []
    return left + right

class State(TypedDict):
    value: Annotated[list[int], NodeReducer]
    


graph = NewGraph(State)

print(graph.invoke({"value": None}))



