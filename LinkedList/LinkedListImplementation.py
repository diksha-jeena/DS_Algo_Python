class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

node1 = Node(1)
print("Node 1 data:" , node1.data)

node2 = Node(5)
node1.next = node2
print("Node 2 data:" , node2.data)

node3 = Node(3)
node2.next = node3
print("Node 3 data:" , node3.data)

current = node1
while current:
    print("Current Node data :" , current.data)
    current = current.next