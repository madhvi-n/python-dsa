"""
Multiplication of linked list with integer
l1 : 2 -> 0 ->
l2 : 3

Output : 6 -> 0 ->
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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


def multiply_with_int(head, k):
    if k > 9:
        raise ValueError(f"k should not be greater than 9")

    if head is None or k == 0:
        return None

    if k == 1:
        return head

    rll = reverse(head)
    prev, curr = None, rll
    carry = 0

    while curr:
        val = (curr.val * k) + carry
        carry = val // 10
        curr.val = val % 10
        prev = curr
        curr = curr.next

    if carry > 0:
        prev.next = ListNode(carry)

    return reverse(rll)


def multiply(l1, l2):
    pass


def main():
    l1 = ListNode(2)
    l1.next = ListNode(5)
    l1.next.next = ListNode(5)

    print_list(l1)

    node = multiply_with_int(l1, 8)
    print_list(node)

if __name__ == '__main__':
    main()
