"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(8)

    print(max_depth(root))


if __name__ == '__main__':
    main()
