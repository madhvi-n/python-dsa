"""
Write a function that moves the last node to the front in a given Singly Linked List.

Examples:

Input: 1->2->3->4->5
Output: 5->1->2->3->4

Input: 3->8->1->5->7->12
Output: 12->3->8->1->5->7
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val


def traverse(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()


def move_last_to_front(head: ListNode):
    temp = head

    second_last = None
    while temp and temp.next:
        second_last = temp
        temp = temp.next
        
    second_last.next = None
    temp.next = head
    head = temp
    traverse(head)


def main():
    head = ListNode(3)
    head.next = ListNode(8)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(7)
    head.next.next.next.next.next = ListNode(12)
    traverse(head)
    move_last_to_front(head)


if __name__ == '__main__':
    main()