"""
Find the distance between two keys in a binary tree, no parent pointers are given.
The distance between two nodes is the minimum number of edges to be traversed to reach one node from another.

Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
'n1' and 'n2' are the two given keys
'root' is root of given Binary Tree.
'lca' is lowest common ancestor of n1 and n2
Dist(n1, n2) is the distance between n1 and n2..
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    return left or right


def distance(root, node, dist=0):
    if root is None or node is None:
        return 0

    if root == node:
        return dist
    distance(root.left, node, dist + 1)
    distance(root.right, node, dist + 1)


def find_distance(root):
    return


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left.right = TreeNode(8)

    print(distance(root, root.right.left))
    # dist = find_distance(root, 4, 5)
    # print("Distance between node {} & {}: {}".format(4, 5, dist))
    # 
    # dist = find_distance(root, 4, 6)
    # print("Distance between node {} & {}: {}".format(4, 6, dist))
    # 
    # dist = find_distance(root, 3, 4)
    # print("Distance between node {} & {}: {}".format(3, 4, dist))
    # 
    # dist = find_distance(root, 2, 4)
    # print("Distance between node {} & {}: {}".format(2, 4, dist))
    # 
    # dist = find_distance(root, 8, 5)
    # print("Distance between node {} & {}: {}".format(8, 5, dist))


if __name__ == '__main__':
    main()
