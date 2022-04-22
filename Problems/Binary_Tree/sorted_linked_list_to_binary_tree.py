"""
https://practice.geeksforgeeks.org/problems/bst-to-greater-sum-tree/

Given a Singly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Linked List.
Note: There might be nodes with same value.

Example 1:

Input:
Linked List: 1->2->3->4->5->6->7
Output:
4 2 1 3 6 5 7
Explanation :
The BST formed using elements of the
linked list is,
        4
      /   \
     2     6
   /  \   / \
  1   3    5   7
Hence, preorder traversal of this
tree is 4 2 1 3 6 5 7
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sorted_linked_list_to_bst():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
