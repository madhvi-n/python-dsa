"""
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print()

def odd_even_list(head):
    if head is None:
        return None

    odd, even = ListNode(), ListNode()
    oddTail, evenTail = odd, even
    count = 0
    while head:
        if count % 2 != 0:
            oddTail.next = head
            oddTail = oddTail.next
        else:
            evenTail.next = head
            evenTail = evenTail.next
        head = head.next
        count += 1

    oddTail.next = even.next
    evenTail.next = None

    return odd.next


def odd_even_list_by_index(head):
    if head is None:
            return None

    odd, even = ListNode(), ListNode()
    oddTail, evenTail = odd, even

    count = 0
    while head:
        if count % 2 == 0:
            evenTail.next = head
            evenTail = evenTail.next
        else:
            oddTail.next = head
            oddTail = oddTail.next
        head = head.next
        count += 1

    evenTail.next = odd.next
    oddTail.next = None

    return even.next


def main():

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print_list(head)

    # print_list(odd_even_list(head))
    print_list(odd_even_list_by_index(head))


if __name__ == '__main__':
    main()
