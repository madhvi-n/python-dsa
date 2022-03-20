class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}, {self.left}, {self.right} "


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def create_bst(arr):
    root = TreeNode(arr[0])

    for i in range(1, len(arr)):
        insert(root, arr[i])

    return root


def print_tree(root):
    if root is None:
        return

    print(root.val)

    if root.left:
        print_tree(root.left)

    if root.right:
        print_tree(root.right)


def main():
    arr = [1, 2, 3, 4, 6, 8, 7, 8]
    r = create_bst(arr)
    print_tree(r)


if __name__ == '__main__':
    main()
