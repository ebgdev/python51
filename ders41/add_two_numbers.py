class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

l1_node1 = Node(2)
l1_node2 = Node(4)
l1_node3 = Node(3)

l1_node1.next = l1_node2
l1_node2.next = l1_node3


l2_node1 = Node(5)
l2_node2 = Node(6)
l2_node3= Node(4)

l2_node1.next = l2_node2
l2_node2.next = l2_node3


def add_two_numbers(l1_node1,l2_node1):
    num1_lst = [] # ['3','4','2']
    cur = l1_node1
    while cur:
        num1_lst.insert(0,str(cur.value))
        cur = cur.next

    num2_lst = []
    cur = l2_node1
    while cur:
        num2_lst.insert(0,str(cur.value))
        cur = cur.next

    total = int(''.join(num1_lst)) + int(''.join(num2_lst)) # --join--> '342' --int--> 342 , total = 807 --> ['7','0','8']
    total = list(reversed(str(total)))
    temp = Node(total[0])
    head = temp
    for i in range(1,len(total)):
        temp.next = Node(total[i])
        temp = temp.next
    return head

result = add_two_numbers(l1_node1,l2_node1) # Head
# Printing the result (linked list)
cur = result
astr = ''
while cur:
    astr += f" {cur.value} -> "
    cur = cur.next
astr += 'None'


# Print a newline at the end of the output to avoid trailing "->"
print(astr)  # This adds a newline after printing the linked list