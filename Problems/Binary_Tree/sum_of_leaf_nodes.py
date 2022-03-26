"""
Find sum of leaf nodes in a given binary tree.

Input :
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
          \
           8
Output :
Sum = 4 + 5 + 8 + 7 = 24
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    return leaf_sum(root.left) + leaf_sum(root.right)


def leaf_sum_2(root):
    elements = []

    if root.left is None and root.right is None:
        elements.append(root.val)

    if root.left:
        elements += leaf_sum_2(root.left)

    if root.right:
        elements += leaf_sum_2(root.right)

    return sum(elements)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(8)

    print(leaf_sum(root))
    print(leaf_sum_2(root))


if __name__ == '__main__':
    main()
