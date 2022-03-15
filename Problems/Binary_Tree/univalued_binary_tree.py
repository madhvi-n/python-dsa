class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_uni_val_tree(root):
    def helper(root):
        elements = set()

        if root is None:
            return None

        elements.add(root.val)

        if root.left:
            left = helper(root.left)
            elements.update(left)

        if root.right:
            right = helper(root.right)
            elements.update(right)
        return elements

    return len(helper(root)) == 1


def uni_val_tree(root):
    val = root.val
    stack = [root]

    while stack:
        node = stack.pop(0)
        if node.val != val:
            return False

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)
    return True


def main():
    pass


if __name__ == '__main__':
    main()
