"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_by_level(root):
    res = []
    queue = deque([root])

    while queue:
        length = len(queue)
        level = []
        for i in range(length):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            res.append(sum(level)/len(level))
    return res


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.left.left = TreeNode(9)
    root.right.right.left.left.left = TreeNode(10)
    root.right.right.right = TreeNode(11)
    root.right.right.right.left = TreeNode(12)
    root.right.right.right.left.left = TreeNode(13)
    root.right.right.right.left.left.right = TreeNode(14)
    root.right.right.right.right = TreeNode(15)
    root.left.left.left = TreeNode(16)
    root.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)

    print(average_by_level(root))


if __name__ == '__main__':
    main()
