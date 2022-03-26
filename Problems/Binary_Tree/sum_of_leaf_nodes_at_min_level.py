"""
Given a binary tree containing n nodes.
The problem is to get the sum of all the leaf nodes which are at minimum level in the binary tree.

Input :
              1
            /   \
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Output : 11
Leaf nodes 4 and 7 are at minimum level.
Their sum = (4 + 7) = 11.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_level_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    queue = [root]
    level = []
    total = flag = 0

    while not flag:
        for node in queue:
            if not node.left and not node.right:
                total += node.val
                flag = 1
            else:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        queue = level
        level = []
    return total


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.left = TreeNode(8)
    root.right.left.right = TreeNode(9)

    print(min_level_sum(root))


if __name__ == '__main__':
    main()
