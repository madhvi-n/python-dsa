"""
https://www.geeksforgeeks.org/find-pair-given-sum-sorted-singly-linked-without-extra-space/

Find pair for given sum in a sorted singly linked without extra space

Input : head = 3 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 , target = 17.
Output: (6, 11), (7, 10), (8, 9)
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def pair_sum(head: ListNode, target: int):
    result = set()
    hashmap = set()

    temp = head
    while temp:
        diff = target - temp.val
        if diff in hashmap:
            result.add((diff, temp.val))
            hashmap.remove(diff)
        else:
            hashmap.add(temp.val)
        temp = temp.next
    print(result)


def main():
    head = ListNode(3)
    head.next = ListNode(6)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(10)
    head.next.next.next.next.next.next = ListNode(11)

    pair_sum(head, 17)
    pair_sum(head, 13)


if __name__ == '__main__':
    main()