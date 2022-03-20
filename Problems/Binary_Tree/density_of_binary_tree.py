"""
https://www.geeksforgeeks.org/density-of-binary-tree-in-one-traversal/?ref=lbp

Given a Binary Tree, find density of it by doing one traversal of it.

Density of Binary Tree = Size / Height
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def density(root):
    h, s = height(root), size(root)
    return s/h


def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def max_width(root):
    width = 0
    h = height(root)

    for i in range(1, h):
        level_width = get_width(root, i)
        width = max(width, level_width)
    return width


def get_width(root, level):
    if root is None:
        return 0

    if level == 1:
        return 1
    return get_width(root.left, level - 1) + get_width(root.right, level - 1)


def height(root):
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(12)

    print(size(root))
    print(density(root))
    print(height(root))
    print(max_width(root))


if __name__ == '__main__':
    main()
