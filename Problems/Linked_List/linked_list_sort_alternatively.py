"""
Given a Linked list of size N, the list is in alternating ascending and descending orders.
Sort the given linked list in non-decreasing order.
Input:
LinkedList: 1 -> 9 -> 2 -> 8 -> 3 -> 7
Output: 1 2 3 7 8 9
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def print_list(head):
    while head:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print()


def sort_list(head):
    if head is None:
        return None

    asc, desc = ListNode(), ListNode()
    ascending_tail, descending_tail = asc, desc

    count = 0
    while head:
        if count % 2 == 0:
            ascending_tail.next = head
            ascending_tail = ascending_tail.next
        else:
            descending_tail.next = head
            descending_tail = descending_tail.next
        head = head.next
        count += 1

    ascending_tail.next = desc.next
    descending_tail.next = None

    return ascending_tail.next


def main():
    head = ListNode(1)
    head.next = ListNode(9)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(7)

    print_list(head)

    node = sort_list(head)

    print_list(node)


if __name__ == '__main__':
    main()
