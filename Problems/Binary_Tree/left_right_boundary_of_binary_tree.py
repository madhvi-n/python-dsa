class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_boundary(root):
    if root is None:
        return
    res = []
    while root:
        if root.left:
            res.append(root.val)
            root = root.left
        else:
            res.append(root.val)
            root = root.right
    return res


def right_boundary(root):
    if root is None:
        return
    res = []

    while root:
        if root.right:
            res.append(root.val)
            root = root.right
        else:
            res.append(root.val)
            root = root.left
    return res


def main():
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('k')
    root.left.left = TreeNode('c')
    root.left.right = TreeNode('h')
    root.right.left = TreeNode('j')
    root.right.right = TreeNode('l')
    root.left.left.left = TreeNode('d')
    root.left.left.right = TreeNode('g')
    root.right.right.left = TreeNode('m')
    root.right.right.right = TreeNode('n')
    root.left.left.left.right = TreeNode('f')
    root.left.left.left.right.right = TreeNode('e')

    print(left_boundary(root))
    print(right_boundary(root))


if __name__ == '__main__':
    main()
