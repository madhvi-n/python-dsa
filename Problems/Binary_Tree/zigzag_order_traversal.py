"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_traversal(root):
    if root is None:
        return []

    s1 = [root]
    s2 = []
    level = []
    result = []

    while s1 or s2:
        while s1:
            root = s1.pop()
            level.append(root.val)
            if root.left:
                s2.append(root.left)
            if root.right:
                s2.append(root.right)
        result.append(level)
        level = []

        while s2:
            root = s2.pop()
            level.append(root.val)

            if root.right:
                s1.append(root.right)
            if root.left:
                s1.append(root.left)
        if level:
            result.append(level)
            level = []
    return result


def zigzag(root):
    res = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()

            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level:
            res.append(level)

    for i in range(len(res)):
        if i % 2 == 1:
            res[i].reverse()
    return res


def zigzag_traversal_2(root):
    res = []
    queue = [root]

    while queue:
        next_queue = []
        level = []
        for node in queue:
            level.append(node.val)

            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

        if level:
            res.append(level)
        queue = next_queue

    for i in range(len(res)):
        if i % 2 == 1:
            res[i].reverse()
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

    print(zigzag_traversal(root))
    print(zigzag(root))
    print(zigzag_traversal_2(root))


if __name__ == '__main__':
    main()

"""
Output:
Level order: [[1], [2, 3], [4, 5, 6, 7], [16, 17, 8, 11], [18, 19, 9, 12, 15], [10, 13], [14]]

[[1], [3, 2], [4, 5, 6, 7], [11, 8, 17, 16], [18, 19, 9, 12, 15], [13, 10], [14]]
[[1], [3, 2], [4, 5, 6, 7], [11, 8, 17, 16], [18, 19, 9, 12, 15], [13, 10], [14]]
[[1], [3, 2], [4, 5, 6, 7], [11, 8, 17, 16], [18, 19, 9, 12, 15], [13, 10], [14]]
"""
