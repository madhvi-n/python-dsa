"""
https://www.geeksforgeeks.org/add-1-number-represented-linked-list/

Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it. For example 1999 is represented as (1-> 9 -> 9 -> 9) and adding 1 to it should change it to (2-> 0 -> 0 -> 0)
"""


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f"ListNode: {self.val}, next: {self.next}"


def reverse(head):
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


def add_one_to_num(head):
    if head is None:
        return None

    rll = reverse(head)
    prev, curr = None, rll
    carry = 0

    while curr:
        s = curr.val + carry

        if prev is None:
            s += 1

        curr.val = s % 10
        carry = s // 10
        prev = curr
        curr = curr.next

    if carry > 0:
        prev.next = ListNode(carry)
    return reverse(rll)


def main():
    head = ListNode(1)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    head.next.next.next = ListNode(9)

    print_list(head)

    node = add_one_to_num(head)
    print_list(node)


if __name__ == '__main__':
    main()
