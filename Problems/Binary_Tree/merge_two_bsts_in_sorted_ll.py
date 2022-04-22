"""
Merge two binary search trees to form one sorted LL
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_traversal(root):
    elements = []

    if root.left:
        elements += inorder_traversal(root.left)

    elements.append(root.val)

    if root.right:
        elements += inorder_traversal(root.right)
    return elements


def create_list(arr):
    pass


def merge(l1, l2):
    if l1 is None and l2 is None:
        return None


    pass


def merge_bst(root1, root2):
    e1 = inorder_traversal(root1)
    e2 = inorder_traversal(root2)

    l1, l2 = create_list(e1), create_list(e2)

    return merge(l1, l2)


def main():
    pass


if __name__ == '__main__':
    main()
