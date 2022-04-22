"""
https://practice.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/


Given a binary tree with a value associated with each node, we need to choose a subset of these nodes
such that sum of chosen nodes is maximum under a constraint that no two chosen node in subset
should be directly connected that is, if we have taken a node in our sum then we can’t take it's
any children or parents in consideration and vice versa

Input:
        1
      /   \
     2     3
    /     /  \
   4     5    6
Output: 16
Explanation: The maximum sum is sum of
nodes 1 4 5 6 , i.e 16. These nodes are
non adjacent
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def max_sum_of_non_adjacent_nodes():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
