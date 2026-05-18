# Circular Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Creating Nodes       
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a
# Traversal
head = a
temp = head

while True:
    print(temp.data)
    temp = temp.next

    if temp == head:
        break        