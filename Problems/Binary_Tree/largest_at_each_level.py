"""
https://practice.geeksforgeeks.org/problems/largest-value-in-each-level/

Given a binary tree, find the largest value in each level.

Example 1:

Input :
        1
       / \
      2   3

Output : 1 3
Explanation :
There are two levels in the tree :
1. {1}, max = 1
2. {2, 3}, max = 3
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_at_each_level(root):
    queue = [root]
    level = []
    res = []

    while queue:
        max_value = -99999
        for node in queue:
            max_value = max(max_value, node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        queue = level
        level = []
        res.append(max_value)
    return res


def main():
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(2)

    print(max_at_each_level(root))


if __name__ == '__main__':
    main()
