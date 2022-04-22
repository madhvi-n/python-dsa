"""
https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/

Given a binary tree, a target node in the binary tree, and an integer value k,
find all the nodes that are at distance k from the given target node.
No parent pointers are available.

Example 1:

Input:
          20
        /    \
      8       22
    /   \
   4    12
       /   \
      10    14
Target Node = 8
K = 2
Output: 10 14 22
Explanation: The three nodes at distance 2
from node 8 are 10, 14, 22.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_nodes_at_distance():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
