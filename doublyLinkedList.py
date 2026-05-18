# Doubly Linked List
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
# Creating Nodes        
a = Node(5)
b = Node(10)
a.next = b
b.prev = a
# Forward Traversal
temp = a
while temp is not None:
    print(temp.data)
    temp = temp.next

# Backward Traversal
temp = b
while temp is not None:
    print(temp.data)
    temp = temp.prev

