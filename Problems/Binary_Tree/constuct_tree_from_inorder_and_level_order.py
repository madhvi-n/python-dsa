
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(inorder, level_order):
    def helper(inorder):
        if inorder is None:
            return None
        root = TreeNode(level_order.pop(0))
        mid = inorder.index(root.val)

        root.left = helper(inorder[:mid])
        root.right = helper(inorder[mid+1:])
        return root
    helper(inorder)


def main():
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(4)


if __name__ == '__main__':
    main()
