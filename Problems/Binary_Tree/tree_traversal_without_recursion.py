class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    stack, result = [root], []
    while stack:
        curr = stack.pop()
        if curr:
            result.append(curr.val)
            stack += [curr.right, curr.left]
    return result


def inorder(root):
    stack, result = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right
    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(11)
    root.right.right.right.left = TreeNode(12)
    root.right.right.right.right = TreeNode(15)
    root.left.left.left = TreeNode(16)
    root.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)

    print(inorder(root))
    print(preorder(root))


if __name__ == '__main__':
    main()
