from typing import Optional


class Node:
    def __init__(self, value:Optional[int]):
        self.prev = None
        self.value = value
        self.next = None

class DoubelyLinkedList:
    def __init__(self):
        self.head = None
    def create(self, values: list[int])->Optional[Node]:
        if len(values) == 0:
            return None
        curr = self.head
        for value in values:
            node = Node(value=value)
            if not self.head:
                curr = node
                self.head = curr
            else: 
                curr.next = node
                node.prev = curr
                curr = node
        
        return self.head
    
    def display(self):
        curr_node = self.head
        while curr_node:
            print(f"{curr_node.value} => ", end="")
            curr_node = curr_node.next
        print("None")
    
    def reverse(self):
        curr_node = self.head
        prev_node = None
        if not self.head and not self.head.next:
            return 
        
        while curr_node:
            curr_node.prev = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = curr_node.prev
        
        self.head = prev_node
    
    def delete_key(self, key:int):
        """Deletes the all occurance of key in the doubly linked list."""
        curr_node = self.head

        while curr_node:
            if curr_node.value == key:
                if curr_node.prev:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                else:
                    self.head = curr_node.next
                    curr_node.next.prev = None
            curr_node = curr_node.next
    
    def remove_duplicates(self):
        """Removes nodes containing duplicate data"""
        unique= set()
        curr = self.head
        while curr:
            if curr.value in unique:
                curr.prev.next = curr.next
                if curr.next: curr.next.prev = curr.prev
            else:
                unique.add(curr.value)
            curr = curr.next
values_arr = [1,2,13,43,4,3,756,8,76,56,635,548,768,45,5,8,1,1,1,2,2,4,4,5,6,7,7]

dl = DoubelyLinkedList()
dl.create(values=values_arr)
dl.display()
dl.reverse()
dl.display()
dl.delete_key(8)
dl.display()
dl.delete_key(5)
dl.display()
dl.remove_duplicates()
dl.display()