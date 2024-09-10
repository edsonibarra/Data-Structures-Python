# Implementation of a binary tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None # The left child of the node
        self.right = None # The right child of the node


# Implementation of a Binary Tree
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


# Add nodes to the Binary Tree
def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
