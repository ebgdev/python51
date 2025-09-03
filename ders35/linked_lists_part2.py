# manual linked lists
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

node5 = Node("mikail",None)
node4 = Node("sevval",node5)
node3 = Node("erfan",node4)
node2 = Node("damla",node3)
node1 = Node("sena",node2)

cur = node1
temp = ""
while cur:
    temp += f"{cur.data} --> "
    cur = cur.next
temp += "None"

print(temp)


