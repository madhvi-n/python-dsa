"""
Find sum of leaf nodes in left subtree of a given binary tree.

Input :
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
          \
           8
Output :
Sum = 4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_sum(root, left):
    if root is None:
        return 0

    if root.left is None and root.right is None and left:
        return root.val

    return leaf_sum(root.left, True) + leaf_sum(root.right, False)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(8)

    print(leaf_sum(root, False))


if __name__ == '__main__':
    main()
