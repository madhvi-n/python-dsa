class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def check_symmetric(subtree_1, subtree_2):
        if not subtree_1 and not subtree_2:
            return True

        if not subtree_1 or not subtree_2:
            return False

        return (subtree_1.val == subtree_2.val
                and check_symmetric(subtree_1.left, subtree_2.right)
                and check_symmetric(subtree_1.right, subtree_2.left)
                )

    return not root or check_symmetric(root.left, root.right)

# The time complexity and space complexity are O(n) and O(h), respectively, where n is the number
# of nodes in the tree and h is the height of the tree


def main():
    root = TreeNode(1)
    root.left = root.right = TreeNode(2)
    root.left.left = root.right.right = TreeNode(3)
    root.left.right = root.right.left = TreeNode(4)
    print(is_symmetric(root))

    root = TreeNode(1)
    root.left = root.right = TreeNode(2)
    root.left.left = root.right.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    print(is_symmetric(root))


if __name__ == '__main__':
    main()
