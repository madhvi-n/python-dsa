class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(f"None \n")


def clone_list(head):
    current = head  # used to iterate over the original list
    dummy = ListNode()  # build the new list of this dummy node

    # point to the last node in a new list
    tail = dummy  # start the tail pointing at the dummy

    while current:
        tail.next = ListNode(current.val, tail.next)  # add each node at the tail
        tail = tail.next  # advance the tail to the new last node
        current = current.next

    return dummy.next


def clone_list_recursive(head):
    if head is None:
        return

    new_node = ListNode(head.val)
    new_node.next = clone_list_recursive(head.next)
    return new_node


def main():
    head = None
    for i in reversed(range(6)):
        head = ListNode(i + 1, head)

    print_list(head)
    node = clone_list(head)
    print_list(node)

    node = clone_list_recursive(head)
    print_list(node)


if __name__ == '__main__':
    main()
