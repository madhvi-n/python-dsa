"""
https://practice.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/

Given an array of size N that can be used to represent a tree.
The array indexes are values in tree nodes and array values give the parent node of that
particular index (or node). The value of the root node index would always be -1 as there is no parent for root.
Construct the standard linked representation of Binary Tree from this array representation.

Note: If two elements have the same parent, the one that appears first in the array will
be the left child and the other is the right child.


Example 1:

Input:
N = 7
parent[] = {-1,0,0,1,1,3,5}
Output: 0 1 2 3 4 5 6
Explanation: the tree generated
will have a structure like
          0
        /   \
       1     2
      / \
     3   4
    /
   5
 /
6
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def construct():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
