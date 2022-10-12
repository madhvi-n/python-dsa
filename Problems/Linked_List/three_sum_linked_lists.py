"""
https://www.geeksforgeeks.org/find-a-triplet-from-three-linked-lists-with-sum-equal-to-a-given-number/
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


# The function assumes that the list b is sorted in ascending order and c is sorted in descending order.
def triplet_sum(first_head: ListNode, second_head: ListNode, third_head: ListNode, target: int) -> bool:
    a = first_head

    while first_head:
        b = second_head
        c = third_head

        # for every node from a, pick a node from b and c
        while b and c:
            total = a.val + b.val + c.val
            if total == target:
                print([a.val, b.val, c.val])
                return True
            elif total < target:
                b = b.next
            else:
                c = c.next
        a = a.next
    return False


def main():
    first = ListNode(20)
    first.next = ListNode(4)
    first.next.next = ListNode(15)
    first.next.next.next = ListNode(8)

    second = ListNode(4)
    second.next = ListNode(6)
    second.next.next = ListNode(7)
    second.next.next.next = ListNode(10)

    third = ListNode(10)
    third.next = ListNode(6)
    third.next.next = ListNode(5)
    third.next.next.next = ListNode(3)

    triplet_sum(first, second, third, 15)
    triplet_sum(first, second, third, 16)
    triplet_sum(first, second, third, 30)
    triplet_sum(first, second, third, 40)


if __name__ == '__main__':
    main()