class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value=None):
        self.head = None
        self.tail = None
        self.length = 0
        
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1

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

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
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
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def basic_get(self,index):
        if index < 0 or index >= self.length:
            return None

        cur = self.head
        pos = 0
        while pos != index:
            cur = cur.next
            pos = pos+1
        return cur
    
    def advanced_get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length//2: 
            print("head'den ileleyerek")
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            print("Tail'den geri gelerek")
            cur = self.tail
            for _ in range(self.length-1,index,-1):
                cur = cur.prev
        
        return cur
    
    def set_value(self,index,n_value):
        cur = self.advanced_get(index)
        if cur:
            cur.value = n_value
            return True
        return False
    

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.advanced_get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after

        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True



    def print_list(self):
        if not self.head:
            return "None"
        astr = " None <--> "
        cur = self.head
        while cur:
            astr += f"{cur.value} <--> "
            cur = cur.next
        astr += "None"
        return astr

        
dl = DoublyLinkedList("erfan")
dl.append("mikail")
dl.append("damla")
dl.append("sena")
dl.append("sevval")
dl.prepend("deneme")
# dl.pop()
# dl.pop_first()
# print(dl.basic_get(8)) --> wrong index , linked list's length is : xxx
print(dl.basic_get(2))
print(dl.advanced_get(2))
print(dl.advanced_get(5))
dl.set_value(0,"emir")
dl.insert(5,"onur")
print(dl.print_list())