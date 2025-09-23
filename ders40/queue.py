class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value=None):
        self.first = None
        self.last = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1

    # Kuyruğa ekleme (sona)
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # Kuyruktan çıkarma (başta)
    def dequeue(self):
        if self.length == 0:
            print("Queue is empty!!!")
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp.value

    # Kuyruğu yazdırma
    def print_queue(self):
        if self.length == 0:
            print('Queue is empty!!!')
            return None
        
        cur = self.first
        my_arr = []
        while cur:
            my_arr.append(str(cur.value))
            cur = cur.next

        return " <-- ".join(my_arr)


# Test
q = Queue()
q.dequeue()  # Boş kuyruğa dequeue denemesi
q.enqueue('value1')
q.enqueue('value2')
q.enqueue('value3')
q.dequeue()
q.enqueue('value4')
q.enqueue('value5')
q.enqueue('value6')

print(q.print_queue())
