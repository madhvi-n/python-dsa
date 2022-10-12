class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


def insert(head, node):
    pass


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(7)
    insert(head, Node(0))
    insert(head, Node(2))
    insert(head, Node(4))
    insert(head, Node(6))
    insert(head, Node(10))


if __name__ == '__main__':
    main()
