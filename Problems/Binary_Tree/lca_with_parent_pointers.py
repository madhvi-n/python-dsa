"""
Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each
node has a parent pointer.

Time: O(h)
Space: O(1)
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"{self.val}"


def lowest_common_ancestor(p, q):

    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    p_depth, q_depth = get_depth(p), get_depth(q)
    if q_depth > p_depth:
        p, q = q, p

    depth_diff = abs(p_depth - q_depth)

    while depth_diff:
        p = p.parent
        depth_diff -= 1

    while p is not q:
        p, q = p.parent, q.parent

    return p


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(12)

    print(lowest_common_ancestor(root.right, root.left.left))
    print(lowest_common_ancestor(root.right.left, root.right.right.right))


if __name__ == '__main__':
    main()
