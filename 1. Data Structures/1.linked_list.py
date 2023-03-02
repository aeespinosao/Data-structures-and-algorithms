from __future__ import annotations

class Node:
    value: int
    next: Node
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class LinkedList:
    head: Node
    tail: Node
    length: int
    
    def __init__(self, value) -> None:
        node: Node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
        
    def print_list(self):
        current: Node = self.head
        while current:
            print(current.value)
            current = current.next
            
    def append(self, value):
        node: Node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def pop(self):
        
        if self.length == 0:
            return
        
        current: Node = self.head
        before_current: Node = None
        
        while current.next:
            before_current = current
            current = current.next
        
        self.tail = before_current
        before_current.next = None
        self.length -= 1      
        
        if self.length == 0:
            self.tail = None
            self.head = None
            
        
    def prepend(self, value):
        node: Node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0:
            return None
        current: Node = self.head
        next_head: Node = current.next
        current.next = None
        self.head = next_head
        self.length -= 1
        
    def get(self, index):
        movements = 0
        current: Node =  self.head
        while movements != index:
            current = current.next
            movements += 1
            
        return current
    
    def set_value(self, index, value):
        node: Node = self.get(index)
        if node:
            node.value = value
    
    def insert(self, index, value):
        new_node: Node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        
        node_before: Node = self.get(index-1)
        new_node.next = node_before.next
        node_before.next = new_node
        self.length += 1
        
    def remove(self, index):
        if index == 0 :
            current: Node = self.head
            self.head = current.next
            current.next = None
            self.length -= 1
            return current
        
        node_before: Node = self.get(index-1)
        current: Node = node_before.next
        node_before.next = current.next
        current.next = None
        self.length -= 1
        return current
    
    def reverse(self):
        before_node: Node = None
        temp: Node = self.head

        while temp.next != None:
            next_node: Node = temp.next
            temp.next = before_node
            before_node = temp
            temp = next_node
        
        temp.next = before_node
        temp = self.tail
        self.tail = self.head
        self.head = temp
            
            
            
        
            
    
if __name__ == '__main__':
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)

    print('LL before reverse():')
    my_linked_list.print_list()

    my_linked_list.reverse()

    print('\nLL after reverse():')
    my_linked_list.print_list()