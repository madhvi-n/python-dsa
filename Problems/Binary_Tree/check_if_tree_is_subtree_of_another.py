"""
https://practice.geeksforgeeks.org/problems/check-if-subtree/

Given two binary trees with head reference as T and S having at most N nodes.
The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a node in T1 and all of its descendants in T1.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root2.right, root2.right)


def check_subtree(tree, subtree):
    if tree is None and subtree is None:
        return True

    if subtree is None:
        return False

    if is_identical(tree, subtree):
        return True

    return check_subtree(tree.left, subtree) or check_subtree(tree.right, subtree)


def main():
    t1 = TreeNode('a')
    t1.left = TreeNode('b')
    t1.left.left = TreeNode('d')
    t1.left.right = TreeNode('e')
    t1.right = TreeNode('c')
    t1.right.left = TreeNode('f')
    t1.right.right = TreeNode('g')
    t1.right.right.left = TreeNode('j')
    t1.right.right.right = TreeNode('k')

    t2 = TreeNode('b')
    t2.left = TreeNode('d')
    t2.right = TreeNode('e')
    t2.right.left = TreeNode('f')

    print(check_subtree(t1, t2))


if __name__ == '__main__':
    main()
