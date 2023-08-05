class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traverse(self):
        if self.root:
            temp = self.root

            print(temp.data, end=" ")

            left_tree = BinaryTree()
            left_tree.root = temp.left

            left_tree.pre_order_traverse()

            right_tree = BinaryTree()
            right_tree.root = temp.right

            right_tree.pre_order_traverse()

    def in_order_traverse(self):
        if self.root:
            temp = self.root

            left_tree = BinaryTree()
            left_tree.root = temp.left

            left_tree.in_order_traverse()

            print(temp.data, end=" ")

            right_tree = BinaryTree()
            right_tree.root = temp.right

            right_tree.in_order_traverse()


    def post_order_traverse(self):
        if self.root:
            temp = self.root

            left_tree = BinaryTree()
            left_tree.root = temp.left

            left_tree.post_order_traverse()


            right_tree = BinaryTree()
            right_tree.root = temp.right

            right_tree.post_order_traverse()

            print(temp.data, end=" ")
    
tree = BinaryTree()

root = Node(1)
tree.root = root

root_left = Node(2)
root.left = root_left

root_right = Node(3)
root.right = root_right

root_left_left = Node(4)
root_left.left = root_left_left

root_left_right = Node(5)
root_left.right = root_left_right

root_right_left = Node(6)
root_right.left = root_right_left

root_right_right = Node(7)
root_right.right = root_right_right

print("Pre-order traversal is: ")
tree.pre_order_traverse()

print("\n\n\nIn-order traversal is: ")
tree.in_order_traverse()

print("\n\n\nPost-order traversal is: ")
tree.post_order_traverse()