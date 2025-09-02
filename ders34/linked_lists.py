class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_to_end(self,n_data):
        new_node = Node(n_data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return 
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.length += 1

    def add_to_begin(self,n_data):
        new_node = Node(n_data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_to_index(self,index,n_data):
        if index < 0 or index > self.length:
            raise IndexError(f"index: {index} out of bounds for {self.length}")
        if index == 0: #(if self.head is None)
            self.add_to_begin(n_data)
            return
        
        new_node = Node(n_data)
        position = 0
        cur = self.head
        while position < index-1:
            position += 1
            cur = cur.next
        temp = cur.next
        cur.next = new_node
        new_node.next = temp
        self.length += 1

    def search(self,target_data):
        cur = self.head
        position = 0
        while cur:
            if cur.data == target_data:
                return position
            position += 1
            cur = cur.next    
        return "Not Found"

    def __str__(self):
        parts = []
        cur = self.head
        while cur:
            parts.append(f"{cur.data}")
            cur = cur.next
        return " --> ".join(parts) + " --> None"

    
ll = LinkedList()
ll.add_to_end("firstNode")
ll.add_to_end("secondNode")
ll.add_to_end("thirdNode")
ll.add_to_begin("zeroNode")
ll.add_to_index(3,"newThreeNode")
print(ll)
print(ll.search("thirdNode"))
print(ll.search("thirdeeNode"))
print(ll.search("firstNode"))
