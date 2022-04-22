class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target):
    if not root:
        return

    if not root.left and not root.right:
        return target == root.val
    
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(12)

    print(has_path_sum(root, 14))
    print(has_path_sum(root, 10))


if __name__ == '__main__':
    main()
