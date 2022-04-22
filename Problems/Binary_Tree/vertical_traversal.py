"""
https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/

Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line,
then they should be printed as they appear in level order traversal of the tree.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root):
    h_dist, v_dist = 0, 0
    result = []
    values = {}

    def vertical_order(root, h_dist, v_dist, values):
        if root is None:
            return

        if h_dist in values.keys():
            values[h_dist].append((v_dist, root.val))
        else:
            values[h_dist] = [(v_dist, root.val)]

        vertical_order(root.left, h_dist - 1, v_dist + 1, values)
        vertical_order(root.right, h_dist + 1, v_dist + 1, values)

    vertical_order(root, h_dist, v_dist, values)

    for x in sorted(values.keys()):
        column = [i[1] for i in sorted(values[x])]
        result.append(column)
    return result


def vertical_order(root):
    direction_map = {}
    queue = deque([(root, 0)])
    while queue:
        node, direction = queue.popleft()
        if direction not in direction_map:
            direction_map[direction] = [node.val]
        else:
            direction_map[direction].append((node.val, direction))

        if node.left:
            queue.append((node.left, direction - 1))

        if node.right:
            queue.append((node.right, direction + 1))

    sorted_view = sorted(direction_map.items())
    return [val for direction, val in sorted_view]


def main():
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right.left = TreeNode('f')
    root.right.right = TreeNode('g')
    root.right.right.left = TreeNode('l')
    root.right.right.left.left = TreeNode('n')
    root.right.right.left.left.left = TreeNode('p')
    root.right.right.right = TreeNode('m')
    root.right.right.right.left = TreeNode('q')
    root.right.right.right.left.left = TreeNode('s')
    root.right.right.right.left.left.right = TreeNode('t')
    root.right.right.right.right = TreeNode('r')
    root.left.left.left = TreeNode('h')
    root.left.left.right = TreeNode('i')
    root.left.left.right.left = TreeNode('j')
    root.left.left.right.right = TreeNode('k')

    print(vertical_traversal(root))
    print(vertical_order(root))


if __name__ == '__main__':
    main()
