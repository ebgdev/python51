class Node:
    def __init__(self,data,next=None,prev = None):
        self.data = data
        self.prev = prev
        self.next = next


# Creating nodes (backward linking)
node5 = Node("burak")
node4 = Node("onur",node5)
node5.prev = node4  # Linking back

node3 = Node("feyza",node4)
node4.prev = node3

node2 = Node("mehmet",node3)
node3.prev = node2

node1 = Node("taha",node2)
node2.prev = node1


# Print forward traversal
cur = node1
print("forward traversal ...")

while cur:
    print(f"{cur.data} --> ", end="")
    cur = cur.next
print("None")


# Print backward traversal (starting from the last node)
cur = node5
print("\nBackward Traversal:")
while cur:
    print(f"{cur.data} --> ", end="")
    cur = cur.prev
print("None")