"""
https://practice.geeksforgeeks.org/problems/odd-even-level-difference/


Given a Binary Tree. Find the difference between the sum of node values at
even levels and the sum of node values at the odd levels.

Input:
            10
          /    \
        20      30
       /  \
     40    60

Output: 60

Explanation:
sum at odd levels - sum at even levels
= (10 + 40 +60) - (20 + 30)
= 110 - 50
= 60
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def odd_even_level_difference(root):
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

    odd_count, even_count = 0, 0
    for i in range(len(res)):
        # Considering index differences, list index starting from 0 while tree index starting from 1
        if i % 2 == 1:
            even_count += sum(res[i])
        else:
            odd_count += sum(res[i])
    return odd_count - even_count


def odd_even_level_difference_2(root):
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

    odd_count, even_count = 0, 0
    for i in range(len(res)):
        if i % 2 == 1:
            even_count += sum(res[i])
        else:
            odd_count += sum(res[i])
    return odd_count - even_count


def main():
    tree = TreeNode(10)
    tree.left = TreeNode(20)
    tree.right = TreeNode(30)
    tree.left.left = TreeNode(40)
    tree.left.right = TreeNode(60)

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

    print(odd_even_level_difference(tree))
    print(odd_even_level_difference_2(tree))

    print(odd_even_level_difference(root))
    print(odd_even_level_difference_2(root))


if __name__ == '__main__':
    main()
