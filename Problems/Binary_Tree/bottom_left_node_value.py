"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.
"""
from collections import deque


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_bottom_left_node(root):
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
            res.append(level)
    return res[-1][0]


def bottom_left_node(root):
    queue = deque()
    queue.append(root)
    left = None

    while queue:
        left = queue[0].val
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return left


def main():
    pass


if __name__ == '__main__':
    main()
