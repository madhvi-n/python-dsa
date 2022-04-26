class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(f"None \n")


def delete_list(head):
    while head:
        print(f"Deleting {head.val} node")
        head = head.next

    if head is None:
        print(f"List deleted")


def main():
    head = None
    for i in reversed(range(6)):
        head = ListNode(i + 1, head)

    print_list(head)
    delete_list(head)


if __name__ == '__main__':
    main()
