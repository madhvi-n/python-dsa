"""
https://practice.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/

Given a binary tree and data value of two of its nodes.
Find the number of turns needed to reach from one node to another in the given binary tree.

Example 1:

Input:
Tree =
           1
        /    \
       2       3
     /  \     /   \
    4    5   6    7
   /        / \
  8        9   10
first node = 5
second node = 10
Output: 4
Explanation:
Turns will be at 2, 1, 3, 6.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def no_of_turns():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
