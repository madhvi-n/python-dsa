"""
Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves should
appear in left-to-right order.

Time: O(n)
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_from_leaves(node):
    if not node:
        return []

    if not node.left and not node.right:
        return [node]

    return list_from_leaves(node.left) + list_from_leaves(node.right)


def main():
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(4)

    print(list_from_leaves(root))


if __name__ == '__main__':
    main()
