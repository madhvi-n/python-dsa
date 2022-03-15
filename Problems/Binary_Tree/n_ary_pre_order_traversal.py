class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def n_ary_preorder_traversal(root):
    elements = []

    if root is None:
        return None

    elements.append(root.val)

    if root.children:
        for children in root.children:
            elements += n_ary_preorder_traversal(children)

    return elements


def preorder(root):
    if not root:
        return []

    stack, result = [root], []

    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(node.children[::-1])
    return result


def main():
    pass


if __name__ == '__main__':
    main()
