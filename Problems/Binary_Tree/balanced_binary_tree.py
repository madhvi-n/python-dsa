"""
Check if the given binary tree is balanced or not

The program implements a postorder traversal with some calls possibly being eliminated because
of early termination. Specifically, if any left subtree is not height-balanced we do not need to visit
the corresponding right subtree. The function call stack corresponds to a sequence of calls from the
root through the unique path to the current node, and the stack height is therefore bounded by the
height of the tree, leading to an O(h) space bound. The time complexity is the same as that for a
postorder traversal, namely O(n).
"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced_tree(tree):
    balanced_tree_status = namedtuple('balanced_tree_status', ('is_balanced', 'height'))

    def check_balanced(node):
        if not node:
            return balanced_tree_status(True, -1)

        left_tree = check_balanced(node.left)
        if not left_tree.is_balanced:
            return balanced_tree_status(False, 0)

        right_tree = check_balanced(node.right)
        if not right_tree.is_balanced:
            return balanced_tree_status(False, 0)

        is_balanced = abs(left_tree.height - right_tree.height) <= 1
        height = max(left_tree.height, right_tree.height) + 1
        return balanced_tree_status(is_balanced, height)

    return check_balanced(tree).is_balanced


def main():
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('k')
    root.right.left = TreeNode('l')
    root.right.right = TreeNode('o')
    root.right.left.left = TreeNode('m')
    root.right.left.right = TreeNode('n')
    root.left.left = TreeNode('c')
    root.left.right = TreeNode('h')
    root.left.right.left = TreeNode('i')
    root.left.right.right = TreeNode('j')
    root.left.left.left = TreeNode('d')
    root.left.left.right = TreeNode('g')
    root.left.left.left.left = TreeNode('e')
    root.left.left.left.right = TreeNode('f')
    print(is_balanced_tree(root))


if __name__ == '__main__':
    main()
