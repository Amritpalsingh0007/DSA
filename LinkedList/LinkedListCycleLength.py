from typing import Optional, Tuple


class Node:
    def __init__(self, value: int | None = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, values: list)->Optional[Node]:
        prev_node = None
        for i in values:
            node = Node(value=i)
            if prev_node:
                prev_node.next = node
                prev_node = node

            if not self.head:
                self.head = node
                prev_node = node
            
        return self.head
    
    def display(self)->None:
        node = self.head
        while node:
            print(f"{node.value} => ",end="")
            node = node.next
        print("None")
    
    def containLoop(self)->bool:
        if not self.head or not self.head.next:
            return False
        slow = self.head
        fast = slow.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow ==fast:
                return True
        return False
    
    def startingNodeOfLoop(self) -> Tuple[Optional[Node], int]:
        if not self.head or not self.head.next:
            return None, -1
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast: return None, -1
        slow = self.head
        index = 0
        while slow != fast:
            slow = slow.next
            fast = fast.next
            index += 1
        return slow, index
    
    def createLoop(self, index:int):
        if not self.head:
            raise IndexError()
        node = self.head
        loop_node = None
        prev_node = None
        while node:
            prev_node = node
            node = node.next
            index -= 1
            if index == 0:
                loop_node = node
        if index > 0:
            raise IndexError()
        else:
            prev_node.next = loop_node

    def loopLength(self)->int:
        if not self.head or not self.head.next:
            return -1
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return -1
        slow = slow.next
        length = 1
        while slow != fast:
            slow = slow.next
            length += 1
        return length
    
    def oddEvenList(self) -> Optional[Node]:
        if not self.head or not self.head.next:
            return self.head

        even_head = self.head.next
        even = even_head
        odd = self.head

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return self.head
values = [1,2,3,4,5,67,6,5,6,8,984,657,54,9,346,234,8,768,5,7,3,64,7]

linked_list = LinkedList()
linked_list.create(values=values)
linked_list.display()
linked_list.oddEvenList()
linked_list.display()
print(linked_list.containLoop())
linked_list.createLoop(index=4)
print(linked_list.containLoop())
print(linked_list.startingNodeOfLoop())
print(linked_list.loopLength())