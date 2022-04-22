"""
Given a binary tree, the print vertical sum of it.
Assume the left and right child of a node makes a 45–degree angle with the parent.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_sum(root):
    d = {}
    res = []

    def helper(node, dist, values):
        if not node:
            return
        values[dist] = values.get(dist, 0) + node.val
        helper(node.left, dist - 1, values)
        helper(node.right, dist + 1, values)

    helper(root, 0, d)

    for key in sorted(d.keys()):
        res.append(d.get(key))
    return res


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print(vertical_sum(root))


if __name__ == '__main__':
    main()
