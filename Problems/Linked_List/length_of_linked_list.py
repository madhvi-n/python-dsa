class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def length(head: Node) -> int:
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def recursive_length(head: Node) -> int:
    def get_count(node: Node) -> int:
        if not node:
            return 0
        return 1 + get_count(node.next)
    return get_count(head)


def recursive_length2(head: Node) -> int:
    def get_count(node: Node, count=0):
        if not node:
            return count
        return get_count(node.next, count + 1)
    return get_count(head)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    print(length(head))
    print(recursive_length(head))
    print(recursive_length2(head))


if __name__ == '__main__':
    main()