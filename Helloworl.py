class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # the pointer initially points to nothing


node1 = Node("Java")
node2 = Node("Python")
node3 = Node("C++")
node1.next = node2
node2.next = node3


