
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_sum(root, partial_sum=0):
    if not root:
        return 0

    partial_sum = partial_sum * 2 + root.val

    if not root.left and not root.right:
        return partial_sum

    return binary_sum(root.left, partial_sum) + binary_sum(root.right, partial_sum)


def main():
    pass


if __name__ == '__main__':
    main()
