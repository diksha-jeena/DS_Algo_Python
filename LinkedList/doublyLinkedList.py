class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(1)
print("Node 1 data:" , node1.data)

node2 = Node(5)
node1.next = node2
node2.prev = node1
print("Node 2 data:" , node2.data)

node3 = Node(3)
node2.next = node3
node3.prev = node2
print("Node 3 data:" , node3.data)

print("Traversing forward")
current = node1   
while current:
    print("Current Node data :" , current.data)
    current = current.next

print("Traversing backward")
current = node3
while current:
    print("Current node data :" , current.data)
    current = current.prev