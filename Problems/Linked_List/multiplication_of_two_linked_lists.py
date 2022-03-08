"""
Multiplication of two linked lists

L1 : 1 -> 2 -> 3 ->
l2 :
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode: {self.val}, next: {self.next}"


def print_list(head):
    if head is None:
        return

    while head:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print()


def multiply(l1, l2):
    num1, num2 = 0, 0

    while l1:
        num1 = (num1 * 10) + l1.val
        l1 = l1.next

    while l2:
        num2 = (num2 * 10) + l2.val
        l2 = l2.next

    return num1 * num2

def main():

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(2)
    l2.next = ListNode(0)

    print_list(l1)
    print_list(l2)

    mul = multiply(l1, l2)

    print(mul)


if __name__ == '__main__':
    main()
