class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def search_iterative(head: Node, key: int) -> bool:
    current = head
    while current:
        if current.val == key:
            return True
        current = current.next
    return False


def recursive_search(head: Node, key: int) -> bool:
    if head is None:
        return False
    if head.val == key:
        return True
    return recursive_search(head.next, key)


def main():
    head = Node(11)
    head.next = Node(26)
    head.next.next = Node(30)
    head.next.next.next = Node(14)
    head.next.next.next.next = Node(9)
    print(search_iterative(head, 30))
    print(search_iterative(head, 3))
    print(recursive_search(head, 30))
    print(recursive_search(head, 3))


if __name__ == '__main__':
    main()
