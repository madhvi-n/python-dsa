
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def main():
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)

    print(is_same_tree(root1, root2))
    print(is_same_tree(root1, root))


if __name__ == '__main__':
    main()
