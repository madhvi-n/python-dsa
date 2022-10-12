class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(f"None \n")


def remove_nth(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Iterate right till n is greater than 0
    while n > 0 and right:
        right = right.next
        n -= 1

    # Shift left and right together until right
    # In the end, left will have previous node of nth and right will be the next node of nth
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)
    print_list(remove_nth(head, 2))


if __name__ == '__main__':
    main()
