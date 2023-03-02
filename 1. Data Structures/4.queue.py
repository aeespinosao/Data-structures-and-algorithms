from __future__ import annotations

class Node:
    value: int
    next: Node
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Queue:
    first: Node
    last: Node
    
    
    def __init__(self, value) -> None:
        node: Node = Node(value)
        self.first = node
        self.last = node
        self.length = 1
        
    def enqueue(self, value) -> None:
        node: Node  = Node(value)
        self.last.next = node
        self.last = node
        self.length += 1
        
    def dequeue(self) -> Node:
        if self.length == 0:
            return None
        node: Node = self.first
        self.first = node.next
        node.next = None
        self.length -= 1
        return node
    