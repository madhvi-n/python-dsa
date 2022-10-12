"""

"""

from collections import deque


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to print reverse level order traversal of a given binary tree
def reverse_level_order(root):
    if root is None:
        return

    # create an empty queue and enqueue the root node
    queue = deque([root])

    # create a stack to reverse level order nodes
    stack = deque()

    while queue:

        # process each node in the queue and enqueue their children
        curr = queue.popleft()

        # push the current node into the stack
        stack.append(curr.val)

        # it is important to process the right node before the left node
        if curr.right:
            queue.append(curr.right)

        if curr.left:
            queue.append(curr.left)

    # pop all nodes from the stack and print them
    while stack:
        print(stack.pop(), end=" ")


def main():
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    reverse_level_order(root)


if __name__ == '__main__':
    main()
