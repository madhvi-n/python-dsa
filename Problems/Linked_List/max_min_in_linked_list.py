"""
Given a singly linked list of n nodes and find the smallest and largest elements in linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(f" {head.val} ->", end=" ")
        head = head.next
    print()


def min_max(head):
    minVal, maxVal = 0, 0

    while head:
        minVal = min(minVal, head.val)
        maxVal = max(maxVal, head.val)
        head = head.next

    return [minVal, maxVal]


def min_max_2(head):
    minVal, maxVal = 0, 0

    while head:
        minVal = minVal if head.val > minVal else head.val
        maxVal = maxVal if head.val < maxVal else head.val
        head = head.next
    return [minVal, maxVal]


def main():
    nums = [8, 2, 4, 5, 7, 9, 12, 2, 1]
    head = ListNode(10)
    for num in nums:
        node = ListNode(num, head)
        head = node

    print_list(head)
    print(min_max(head))
    print(min_max_2(head))

if __name__ == '__main__':
    main()
