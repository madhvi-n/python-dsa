"""
https://practice.geeksforgeeks.org/problems/sum-tree/

Given a Binary Tree. Return true if, for every node X in the tree other than the leaves,
its value is equal to the sum of its left subtree's value and its right subtree's value. Else return false.

An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0.
A leaf node is also considered a Sum Tree.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_sum_tree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    left =  add(root.left)
    right = add(root.right)

    total = left + right

    if root.val == total :
        if is_sum_tree(root.left) and is_sum_tree(root.right):
            return True
    return False


def add(node):
    if node is None:
        return 0
    return node.val + add(node.left) + add(node.right)


def main():
    root = TreeNode(56)
    root.left = TreeNode(13)
    root.right = TreeNode(15)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(2)
    root.right.right.right = TreeNode(1)

    print(is_sum_tree(root))


if __name__ == '__main__':
    main()
