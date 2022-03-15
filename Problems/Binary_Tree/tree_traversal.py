class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    elements = []
    if root is None:
        return None

    if root.left:
        elements += inorder(root.left)

    elements.append(root.val)

    if root.right:
        elements += inorder(root.right)
    return elements


def preorder(root):
    elements = []
    if root is None:
        return None

    elements.append(root.val)

    if root.left:
        elements += preorder(root.left)

    if root.right:
        elements += preorder(root.right)
    return elements


def postorder(root):
    elements = []
    if root is None:
        return None

    if root.left:
        elements += postorder(root.left)

    if root.right:
        elements += postorder(root.right)

    elements.append(root.val)
    return elements


def main():
    pass


if __name__ == '__main__':
    main()
