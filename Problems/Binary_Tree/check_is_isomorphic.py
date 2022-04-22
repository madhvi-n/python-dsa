"""
Check if two binary trees are isomorphic
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    first = is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right)
    second = is_isomorphic(root1.right, root2.left) and is_isomorphic(root1.left, root2.right)

    if first or second:
        return True
    return False


def main():
    root1 = TreeNode('a')
    root1.left = TreeNode('b')
    root1.right = TreeNode('c')
    root1.left.left = TreeNode('d')
    root1.left.right = TreeNode('e')
    root1.left.right.left = TreeNode('f')
    root1.left.right.right = TreeNode('g')

    root2 = TreeNode('a')
    root2.left = TreeNode('c')
    root2.right = TreeNode('b')
    root2.right.left = TreeNode('e')
    root2.right.right = TreeNode('d')
    root2.right.left.left = TreeNode('g')
    root2.right.left.right = TreeNode('f')

    print(is_isomorphic(root1, root2))


if __name__ == '__main__':
    main()
