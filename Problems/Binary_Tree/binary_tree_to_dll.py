"""
https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def convert(root):
    result = []

    if not root:
        return []

    if root.left:
        result += convert(root.left)

    result.append(root)

    if root.right:
        result += convert(root.right)
    return result


def main():
    pass


if __name__ == '__main__':
    main()
