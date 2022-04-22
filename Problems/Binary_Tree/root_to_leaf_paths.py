"""
Print all root to leaf paths in a binary tree.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_leaf(root):
    pass


def print_stack(stack):
    for i in range(len(stack), -1):
        stack.pop(i)
        print(stack[i], end=" ")


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(12)

    print(root_to_leaf(root))


if __name__ == '__main__':
    main()
