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
        """
        Root->Left->Right
        """
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def in_order_print(self, start: Node, traversal: str) -> str:
        """
        In-Order Traversal Algorithm:

        Left->Root->Right

        1. Check if the current node is empty/None.
        2. Traverse the left subtree by recursively calling
        the in-order method.
        3. Display the data part of the root (or the current node).
        4. Traverse the right subtree by recursively calling
        the in-order method.
        """
        if start:
            traversal =  self.in_order_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.in_order_print(start.right, traversal)
        return traversal
    
    def post_order_print(self, start: Node, traversal: str) -> str:
        """
        Post-Order Traversal Algorithm:

        Left->Right->Root

        1. Check if the current node is empty/None.
        2. Traverse the left subtree by recursively calling
        the post-order method.
        3. Traverse the right subtree by recusively calling
        the post-order method.
        4. Display the data part of the root.
        """
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += str(start.value) + "-"
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
