"""
https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
"""


class ListNode:
    def __init__(self, val=None, next_node=None, child=None):
        self.val = val
        self.next = next_node
        self.child = child

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def flatten(head):
    if not head:
        return

    temp = head
    while temp.next:
        temp = temp.next
    current = head

    while current != temp:
        if current.child:
            temp.next = current.child

            child_node = current.child
            while child_node.next:
                child_node = child_node.next
            temp = child_node
        current = current.next


def print_list(head):
    if head is None:
        return

    while head:
        separator = " -> " if head.next else " "
        print(head.val, end=separator)
        head = head.next
    print()


def main():
    child13 = ListNode(16)
    child13.child = ListNode(3)

    head1 = ListNode(4)
    head1.next = ListNode(20)
    head1.next.child = ListNode(2)
    head1.next.next = ListNode(13)
    head1.next.next.child = child13

    child9 = ListNode(19)
    child9.next = ListNode(15)

    child17 = ListNode(9)
    child17.next = ListNode(8)
    child17.child = child9

    head2 = ListNode(17)
    head2.next = ListNode(6)
    head2.child = child17

    head = ListNode(10)
    head.child = head1
    head.next = ListNode(5)
    head.next.next = ListNode(12)
    head.next.next.next = ListNode(7)
    head.next.next.next.child = head2
    head.next.next.next.next = ListNode(11)

    flatten(head)
    print_list(head)


if __name__ == '__main__':
    main()
