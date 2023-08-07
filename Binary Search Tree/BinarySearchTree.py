class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(root,data):
        

    def in_order_traverse(self):
        if self.root:
            temp = self.root
            temp.left.in_order_traverse()
            print(temp.data, end=" ")
            temp.right.in_order_traverse()


tree = BinarySearchTree()

tree.insert(50)
tree.insert(10)
tree.insert(40)
tree.insert(30)
tree.insert(120)
tree.insert(14)
tree.insert(123)

tree.in_order_traverse()