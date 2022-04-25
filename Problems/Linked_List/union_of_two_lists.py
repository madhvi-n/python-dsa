"""
https://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/

Input:
   List1: 10->15->4->20
   List2:  8->4->2->10
Output:
   Union List: 2->8->20->4->15->10
"""


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return f"{self.val} ->"

    def __repr(self):
        return f"{self.val} -> {self.next}"


def union(head1, head2):
    hash_map = {}
    dummy = ListNode(None)
    prev = dummy

    n1 = head1
    while n1:
        hash_map[n1.val] = 1 + hash_map.get(n1.val, 0)
        n1 = n1.next

    n2 = head2
    while n2:
        hash_map[n2.val] = 1 + hash_map.get(n2.val, 0)
        n2 = n2.next

    for node in hash_map:
        prev.next = ListNode(node)
        prev = prev.next
    return dummy.next


def main():
    head1 = ListNode(10)
    head1.next = ListNode(15)
    head1.next.next = ListNode(4)
    head1.next.next.next = ListNode(20)

    head2 = ListNode(2)
    head2.next = ListNode(4)
    head2.next.next = ListNode(8)
    head2.next.next.next = ListNode(10)
    d = union(head1, head2)

    while d:
        print(f"{d.val} ->", end=" ")
        d = d.next


if __name__ == '__main__':
    main()
