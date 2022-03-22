class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diagonal_sum(root):
    v_dist = 0
    diagonal_count = {}

    def diagonal_order(root, v_dist, diagonal_count):
        if root is None:
            return

        if v_dist in diagonal_count.keys():
            diagonal_count[v_dist] += root.val
        else:
            diagonal_count[v_dist] = root.val

        diagonal_order(root.left, v_dist + 1, diagonal_count)
        diagonal_order(root.right, v_dist, diagonal_count)

    diagonal_order(root, v_dist, diagonal_count)

    return list(diagonal_count.values())


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.left.left = TreeNode(9)
    root.right.right.left.left.left = TreeNode(10)
    root.right.right.right = TreeNode(11)
    root.right.right.right.left = TreeNode(12)
    root.right.right.right.left.left = TreeNode(13)
    root.right.right.right.left.left.right = TreeNode(14)
    root.right.right.right.right = TreeNode(15)
    root.left.left.left = TreeNode(16)
    root.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)

    print(diagonal_sum(root))


if __name__ == '__main__':
    main()
