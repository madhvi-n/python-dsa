from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def n_ary_level_order_traversal(root):
    if not root:
        return None

    res = []
    q = deque([root])

    while q:
        length = len(q)
        level = []
        for i in range(length):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.extend(node.children)
        if level:
            res.append(level)
    return res


def main():
    pass


if __name__ == '__main__':
    main()
