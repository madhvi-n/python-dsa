class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f"ListNode: {self.val}, next: {self.next}"


def recurse_reverse(node):
    if node is None or node.next is None:
        return node

    node1 = recurse_reverse(node.next)
    node.next.next = node
    node.next = None
    return node1


def iter_reverse(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def print_list(head):
    if head is None:
        return

    while head:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print()


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print_list(head)

    h1 = recurse_reverse(head)
    print_list(h1)

    print()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print_list(head)

    h2 = iter_reverse(head)
    print_list(h2)


if __name__ == '__main__':
    main()
