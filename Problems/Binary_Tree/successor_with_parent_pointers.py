"""
Design an algorithm that computes the successor of a node in a binary tree. Assume that each node
stores its parent.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def successor(root):
    if root.right:
        # successor is the leftmost element in node's right subtree
        root = root.right
        while root:
            root = root.left
        return root

    # find the closest ancestor whose left subtree contains node
    while root.parent and root.parent.right is root:
        root = root.parent
    # A return value of None means node does not have successor, i.e. node is rightmost node in the tree
    return root.parent


def main():
    pass


if __name__ == '__main__':
    main()
