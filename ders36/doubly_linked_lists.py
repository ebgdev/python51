from icecream import ic 
from time import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return
    

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    
    def pop(self):
        if self.length == 0:  
            return None

        cur = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            cur.prev = None

        self.length -= 1
        return cur
        
    
    def print_list(self):
        if self.head is None or self.tail is None:
            return "list is empty"
        alist = []
        cur = self.head
        while cur:
            alist.append(str(cur.value))
            cur = cur.next

        return("None <--> " + " <--> ".join(alist) + " <--> None")
    
dl = DoublyLinkedList()
dl.append("deneme1")
dl.append("deneme2")
dl.append("deneme3")
dl.append("deneme4")
dl.pop()
print(dl.print_list())