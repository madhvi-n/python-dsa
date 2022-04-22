"""
https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/

Construct a binary tree of size N using two given arrays pre[] and preLN[].
Arrays pre[] represents preorder traversal of a binary tree.
Arrays preLN[] has only two possible values L and N.
The value L in preLN[] indicates that the corresponding node in Binary Tree is a leaf node
and value N indicates that the corresponding node is a non-leaf node.
Note: Every node in the binary tree has either 0 or 2 children.

Input :
N = 5
pre[] = {10, 30, 20, 5, 15}
preLN[] = {N, N, L, L, L}

Output:
          10
        /    \
      30      15
     /  \
   20    5
"""


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
