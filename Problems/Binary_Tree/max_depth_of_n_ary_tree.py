"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
"""


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children


def max_depth(root):
    if root is None:
        return 0

    depth = 0
    for node in root.children:
        depth = max(depth, max_depth(node))
    return depth + 1


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
