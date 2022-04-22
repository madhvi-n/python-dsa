"""
https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/

Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order:

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node
you could reach when you always travel preferring the left subtree over the right subtree.

Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.

Reverse right boundary nodes: defined as the path from the right-most node to the root.
The right-most node is the leaf node you could reach when you always travel preferring the right subtree
over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundary_traversal(root) -> list:
    if root is None:
        return []

    res = set()
    res.add(root.val)

    def get_left_boundary(root):
        if root is None or root.left is None and root.right is None:
            return
        res.add(root.val)
        if root.left:
            get_left_boundary(root.left)
        else:
            get_left_boundary(root.right)

    def get_right_boundary(root):
        if root is None or root.left is None and root.right is None:
            return
        if root.right:
            get_right_boundary(root.right)
        else:
            get_right_boundary(root.left)
        res.add(root.val)

    def get_leaf_nodes(node):
        if node is None:
            return
        if node.left is None and node.right is None and node != root:
            res.add(node.val)
        get_leaf_nodes(node.left)
        get_leaf_nodes(node.right)

    get_left_boundary(root.left)
    get_leaf_nodes(root)
    get_right_boundary(root.right)
    return list(res)


#  Time: O(n)
def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right

    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (([subtree.val] if is_boundary or is_leaf(subtree) else [])
                + left_boundary_and_leaves(subtree.left, is_boundary)
                + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)
                )

    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right)
                + right_boundary_and_leaves(subtree.right, is_boundary)
                + ([subtree.val] if is_boundary or is_leaf(subtree) else [])
                )

    return ([tree.val] + left_boundary_and_leaves(tree.left, True)
            + right_boundary_and_leaves(tree.right, True) if tree else [])


def main():
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('k')
    root.left.left = TreeNode('c')
    root.left.right = TreeNode('h')
    root.right.left = TreeNode('j')
    root.right.right = TreeNode('l')
    root.left.left.left = TreeNode('d')
    root.left.left.right = TreeNode('g')
    root.right.right.left = TreeNode('m')
    root.right.right.right = TreeNode('n')
    root.left.left.left.right = TreeNode('f')
    root.left.left.left.right.right = TreeNode('e')

    print(boundary_traversal(root))
    print(exterior_binary_tree(root))


if __name__ == '__main__':
    main()
