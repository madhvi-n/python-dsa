"""
Check if two binary trees are identical
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


def main():
    t1 = TreeNode('a')
    t1.left = TreeNode('b')
    t1.right = TreeNode('c')

    t2 = TreeNode('a')
    t2.left = TreeNode('b')
    t2.right = TreeNode('c')

    t3 = TreeNode('a')
    t3.left = TreeNode('b')
    t3.left.left = TreeNode('d')
    t3.right = TreeNode('c')
    t3.left.right = TreeNode('e')

    print(is_identical(t1, t2))
    print(is_identical(t1, t3))


if __name__ == '__main__':
    main()
