"""
https://practice.geeksforgeeks.org/problems/array-to-bst4443/

Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST).
Find the preorder traversal of height balanced BST.
If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Height balanced BST means a binary tree in which the depth of the left subtree and
the right subtree of every node never differ by more than 1.

Hint: if parent node is at index i in the array then the left child of that node is at index (2*i + 1)
and right child is at index (2*i + 2) in the array.

Input: nums = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
Explanation:
The preorder traversal of the following
BST formed is {2, 1, 3, 4}:
           2
         /   \
        1     3
               \
                4
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_bst(arr):
    pass


def print_preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


def main():
    arr = [x for x in range(1, 9)]


if __name__ == '__main__':
    main()
