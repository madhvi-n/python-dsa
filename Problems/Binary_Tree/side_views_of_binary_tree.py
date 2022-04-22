"""
Left and right side view of binary tree.

                    a
                  /   \
                b      c
              / \     / \
            d    e   f   g
          /  \          /  \
         h    i        l   m
             / \      /   /  \
            j   k    n   q   r
                    /   /
                   p    s
                        \
                         t

Left view: a, b, d, h, j, p, t.
Right view: a, c, g, m, r, s, t.
Top view: h, b, d, a, e, g, m, r.
Bottom view: h, j, p, n, s, t, m, r.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root):
    result = []
    queue = [root]
    level = []

    while queue != [] and root is not None:
        nodes = []
        for node in queue:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

            nodes.append(node.val)
        result.append(nodes[0])
        queue = level
        level = []
    return result


def right_view(root):
    result = []
    queue = [root]
    level = []

    while queue != [] and root is not None:
        for node in queue:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        result.append(node.val)
        queue = level
        level = []
    return result


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


def top_view_using_vertical_order(root):
    vertical_order = vertical_traversal(root)
    result = [nodes[0] for nodes in vertical_order]
    return result


def top_view(root):
    direction_map = {}
    queue = deque([(root, 0)])
    while queue:
        node, direction = queue.popleft()
        if direction not in direction_map:
            direction_map[direction] = node.val

        if node.left:
            queue.append((node.left, direction - 1))

        if node.right:
            queue.append((node.right, direction + 1))

    sorted_view = sorted(direction_map.items(), key=lambda x: x[0])
    return [val for direction, val in sorted_view]


def bottom_view(root):
    vertical_order = vertical_traversal(root)
    result = [nodes[-1] for nodes in vertical_order]
    return result


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

    print(f"Left view: {left_view(root)}")
    print(f"Right view: {right_view(root)}")
    print(f"Top view: {top_view(root)}")
    print(f"Top view: {top_view_using_vertical_order(root)}")
    print(f"Bottom view: {bottom_view(root)}")


if __name__ == '__main__':
    main()
