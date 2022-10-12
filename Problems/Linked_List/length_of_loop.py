"""
Find length of loop in linked list

Input: linked list = 1 -> 2 -> 3 -> 4 -> 5 -> 2
Output: 4
Explanation: The loop is present in the below-linked list and the length of the loop is 4.

Input: linked list = 4 -> 3 -> 7 -> 9 -> 2
Output: 0
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def length_of_loop(head: ListNode) -> int:
    pass


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(2)
    print(length_of_loop(head))


if __name__ == '__main__':
    main()