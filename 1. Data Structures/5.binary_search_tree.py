from __future__ import annotations

class Node:
    value: int
    left: Node
    right: Node
    
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    root: Node    
    
    def __init__(self) -> None:
        self.root = None 
        
    def insert(self, value) -> None:
        node: Node = Node(value)
        if self.root is None:
            self.root = node
            return
        current: Node = self.root
        while(True):
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
                
    def contains(self, value) -> bool:
        current: Node = self.root
        while(current is not None):
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else: 
                current = current.right
        return False
    
    def min_value_node(self, value) -> Node:
        current: Node = self.root
        while(current.left is not None):
            current = current.left
        return current