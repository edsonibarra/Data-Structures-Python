from typing import Any


# Implementation of a binary tree node
class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None  # The left child of the node
        self.right = None  # The right child of the node

    def __str__(self) -> str:
        return f"Node: {self.value}"


# Implementation of a Binary Tree
class BinaryTree:
    def __init__(self, root: Any):
        self.root = Node(root)

    def preorder_print(self, start: Node, traversal: str):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Add nodes to the Binary Tree
def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.preorder_print(tree.root, ""))


if __name__ == "__main__":
    main()
