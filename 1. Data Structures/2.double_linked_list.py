from __future__ import annotations

class Node:
    value: int
    next: Node
    prev: Node
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    head: Node
    tail: Node
    length: int
    
    def __init__(self, value) -> None:
        node: Node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
            
    def append(self, value):
        node: Node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next =  node
            node.prev = self.tail
            self.tail = node
        self.length += 1
    
    def pop(self):
        
        if self.length == 0:
            return
        
        if self.length == 1:
            current: Node = self.tail
            self.tail = None
            self.head = None
            return current
        
        current: Node = self.tail
        current.prev.next = None
        self.tail = current.prev
        current.prev = None
        self.length -= 1

        return current
            
        
    def prepend(self, value):
        node: Node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0:
            return None
        current: Node = self.head
        next_head: Node = current.next
        current.next = None
        self.head = next_head
        if next_head:
            next_head.prev = None
        self.length -= 1
        return current
        
    def get(self, index):
        if index < self.length/2:
            movements = 0
            current: Node =  self.head
            while movements != index:
                current = current.next
                movements += 1
        else:
            movements = self.length-1
            current: Node =  self.tail
            while movements != index:
                current = current.prev
                movements -= 1
        return current
    
    def set_value(self, index, value):
        node: Node = self.get(index)
        if node:
            node.value = value
    
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        
        before = self.get(index-1)
        after = before.next
        
        new_node = Node(value)
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1   
        
    def remove(self, index):
        if index == 0 :
            current: Node = self.head
            current.next.prev = None
            self.head = current.next
            current.next = None
            self.length -= 1
            return current
        
        current: Node = self.get(index)
        prev = current.prev
        current.prev.next = current.next
        current.next.prev =prev
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
    my_linked_list = DoublyLinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)

    print('LL before reverse():')
    my_linked_list.print_list()

    my_linked_list.reverse()

    print('\nLL after reverse():')
    my_linked_list.print_list()