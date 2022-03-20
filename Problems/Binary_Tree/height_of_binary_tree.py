"""
https://practice.geeksforgeeks.org/problems/height-of-binary-tree/

"""


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def height(root):
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(12)

    print(height(root))


if __name__ == '__main__':
    main()
