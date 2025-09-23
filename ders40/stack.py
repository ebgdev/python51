class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None):
        self.top = None
        self.height = 0

        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            print("Stack is empty!!!")
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

    def print_stack(self):
        if self.height == 0:
            print("Stack is empty!!!")
            return None
        
        cur = self.top
        my_arr = []
        while cur:
            my_arr.append(str(cur.value))
            cur = cur.next

        return " --> ".join(my_arr)


# Test
stack = Stack('value1')
stack.push('value2')
stack.push('value3')
stack.push('value4')
stack.push('value5')
stack.push('value6')
stack.pop()  # value6 çıkarılır

print(stack.print_stack())
