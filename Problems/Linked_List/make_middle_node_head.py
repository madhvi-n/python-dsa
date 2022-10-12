"""
https://www.geeksforgeeks.org/make-middle-node-head-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def middle_head(head):
    l = length(head)
    mid = l // 2

    prev, middle = None, head
    for i in range(mid):
        prev = middle
        middle = middle.next

    prev.next = middle.next
    middle.next = head
    head = middle
    return head


def print_list(head):
    while head:
        print(f"{head.val} -> ", end=" ")
        head = head.next
    print()


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)
    node = middle_head(head)
    print_list(node)


if __name__ == '__main__':
    main()
