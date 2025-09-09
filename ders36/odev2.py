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
    
    def del_from_begin(self):
        if self.head is None:
            return 
        self.head = self.head.next
        self.length -=1

    def del_from_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            self.length -= 1
        
        cur = self.head
        temp_prev = None
        while cur.next:
            temp_prev = cur
            cur = cur.next
        if temp_prev:
            temp_prev.next = None
    
    # ODEV 2️⃣
    def del_from_index(self,index):
        if index < 0 or index >= self.length:
            raise IndexError("Index Out of Range")
        
        if index == 0:
            deleted_item = self.head
            self.head = self.head.next
            deleted_item.next = None
            self.length -= 1
            return deleted_item.data

        position = 0
        cur = self.head
        while position < index - 1:
            position += 1
            cur = cur.next
        
        deleted_item = cur.next
        cur.next = cur.next.next
        deleted_item.next = None
        self.length -= 1 
        return deleted_item.data



    # reverse LinkedList
    def reverseList(self,head):
        prev , cur = None, head
        while cur:
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev

    def reverse(self):
        self.head = self.reverseList(self.head)

    

    def __str__(self):
        temp = ""
        cur = self.head
        while cur:
            temp += f"{cur.data} --> "
            cur = cur.next
        temp += "None"
        return str(temp)
    
ll = LinkedList()
ll.add_to_end("firstNode")
ll.add_to_end("secondNode")
ll.add_to_end("fourthNode")
ll.add_to_begin("zeroNode")
ll.add_to_index(3,"newThreeNode")
ll.del_from_begin()
ll.del_from_end()
print(ll)
# ll.reverse()
print(ll.del_from_index(0))
print(ll)
# print(ll.search("thirdNode"))
# print(ll.search("thirdeeNode"))
# print(ll.search("firstNode"))
