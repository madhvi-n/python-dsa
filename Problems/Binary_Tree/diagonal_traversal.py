"""
d = diagonal distance
for every left child, d = d + 1
for every right child d = d of parent
"""
from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diagonal_traversal(root):
    h_dist = 0
    result = []
    values = {}

    def diagonal_order(root, h_dist, values):
        if root is None:
            return

        if h_dist in values.keys():
            values[h_dist].append(root.val)
        else:
            values[h_dist] = [root.val]

        diagonal_order(root.left, h_dist + 1, values)
        diagonal_order(root.right, h_dist, values)

    diagonal_order(root, h_dist, values)

    for x in sorted(values.keys()):
        result.append(sorted(values[x]))
    return result


def diagonal(root):
    out = []
    node = root
    # queue to store left nodes
    q = deque()
    while node:
        # append data to output array
        out.append(node.val)
        # if left available add it to the queue
        if node.left:
            q.appendleft(node.left)
        # if right is available change the node
        if node.right:
            node = node.right
        else:
            # else pop the left_q
            if len(q) >= 1:
                node = q.pop()
            else:
                node = None
    return out


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.left.left = TreeNode(9)
    root.right.right.left.left.left = TreeNode(10)
    root.right.right.right = TreeNode(11)
    root.right.right.right.left = TreeNode(12)
    root.right.right.right.left.left = TreeNode(13)
    root.right.right.right.left.left.right = TreeNode(14)
    root.right.right.right.right = TreeNode(15)
    root.left.left.left = TreeNode(16)
    root.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)

    print(diagonal(root))
    print(diagonal_traversal(root))


if __name__ == '__main__':
    main()
