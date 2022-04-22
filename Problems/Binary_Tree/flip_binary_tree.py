"""
https://practice.geeksforgeeks.org/problems/clone-a-binary-tree/

Given a special binary tree having random pointers along with the usual left and right pointers.
Clone the given tree.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def flip_binary_tree(root):
    if root is None:
        return root

    if root.left is None and root.right is None:
        return root

    # Recursively call the same method
    new_root = flip_binary_tree(root.left)

    # Rearranging main root Node
    # after returning from
    # recursive call
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return new_root


def flip_tree_iterative(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return root

    curr, nxt, prev = root, None, None
    temp = None

    while curr:
        nxt = curr.left
        curr.left = temp
        temp = curr.right
        curr.right = prev

        prev = curr
        curr = nxt

    return prev


def main():
    pass


if __name__ == '__main__':
    main()
