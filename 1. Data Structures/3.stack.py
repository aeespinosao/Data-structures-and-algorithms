from __future__ import annotations

class Node:
    value: int
    next: Node
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Stack:
    top: Node
    
    def __init__(self, value) -> None:
        node: Node = Node(value)
        self.top = node
        self.height = 1
        
    def push(self, value) -> None:
        node: Node  = Node(value)
        node.next = self.top
        self.top = node
        self.height += 1
        
    def pop(self) -> Node:
        node: Node = self.top
        if self.height == 1:
            self.top = None
            self.height = 0
            return node
        self.top = node.next
        node.next = None
        self.height -= 1
        return node