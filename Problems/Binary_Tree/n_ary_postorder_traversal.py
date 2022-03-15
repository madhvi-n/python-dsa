class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def n_ary_postorder_traversal(root):
    elements = []

    if root is None:
        return None

    if root.children:
        for children in root.children:
            elements += n_ary_postorder_traversal(children)

    elements.append(root.val)

    return elements


def postorder(root):
    if not root:
        return []
    output = []
    stack = [root]
    while stack:
        root = stack.pop()
        output.append(root.val)
        for child in root.children:
            stack.append(child)
    return output[::-1]


def postorder_using_dfs(root):
    res = []

    def dfs(current_node):
        if current_node:
            if current_node.children:
                for v in current_node.children:
                    dfs(v)
            res.append(current_node.val)

    dfs(root)
    return res


def main():
    pass


if __name__ == '__main__':
    main()
