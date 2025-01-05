from typing_extensions import TypedDict
import random
from typing import Literal

class State(TypedDict):
    graphState: str

def node1(state):
    print("----------node1------------")
    return {"graphState": state["graphState"] + "I am "}

def node2(state):
    print("----------node1------------")
    return {"graphState": state["graphState"] + "happy!"}

def node3(state):
    print("----------node1------------")
    return {"graphState": state["graphState"] + "sad!"}


def decide_mood(state)->Literal["node2", "node3"]:
    rand_float = random.random()
    if rand_float > 0.5:
        return "node2"
    else:
        return "node3"
    
def test():
    print("----------test------------")