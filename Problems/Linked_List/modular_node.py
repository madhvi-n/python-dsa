"""
Given a singly linked list and a number k, find the last node whose n % k == 0, where n is the number of nodes in the list.
Examples:

Input : list = 1->2->3->4->5->6->7, k = 3
Output : 6

Input : list = 3->7->1->9->8, k = 2
Output : 9

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


def modular_node(head, k):
    if head is None:
        return None
    
    prev, curr = None, head

    while curr:
        if curr.val % k == 0:
            prev = curr
        curr = curr.next
    return prev.val


def main():
    nums = [8, 2, 4, 6, 5, 7, 9, 12, 13]
    head = ListNode(10)
    for num in nums:
        node = ListNode(num, head)
        head = node

    print_list(head)
    print(modular_node(head, 2))
    print(modular_node(head, 3))

if __name__ == '__main__':
    main()
