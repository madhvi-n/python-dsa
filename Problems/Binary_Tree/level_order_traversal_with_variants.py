"""
https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/

Given a Binary Tree with all unique values and two nodes value, n1 and n2.
The task is to find the lowest common ancestor of the given two nodes.
We may assume that either both n1 and n2 are present in the tree or none of them are present.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Level order traversal"""
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
    return res


def level_order_2(root):
    result = []
    level = []
    next_queue = []
    queue = [root]

    while queue:
        for node in queue:
            level.append(root.val)
            if node.left:
                next_queue.append(root.left)
            if node.right:
                next_queue.append(root.right)
        result.append(level)
        queue = next_queue
        level = []
        next_queue = []
    return result


def level_order_spiral_traversal(root):
    """Level order traversal in spiral form"""
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


def level_order_with_direction_change(root):
    """Level order traversal with direction change after every two levels"""
    if root is None:
        return None

    if root.left is None and root.right is None:
        print(root.val)

    stack = []
    queue = deque([root])

    pass


def reverse_level_order(root):
    """Reverse level order traversal"""
    queue = deque([root])
    stack = deque()
    res = []

    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.popleft()
            stack.append(node.val)
            if node:
                queue.append(node.right)
                queue.append(node.left)

    if stack:
        for i in range(len(stack)):
            node = stack.pop()
            res.append(node)
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

    # print(level_order_2(root))
    print(reverse_level_order(root))


if __name__ == '__main__':
    main()
