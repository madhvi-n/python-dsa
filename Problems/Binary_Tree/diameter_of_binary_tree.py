class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def diameter(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)
        return 1 + max(left, right)

    dfs(root)
    return res[0]


def main():
    pass


if __name__ == '__main__':
    main()
