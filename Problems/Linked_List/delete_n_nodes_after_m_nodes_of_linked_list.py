"""
Given a linked list and two integers m and  n. Traverse the linked list such that you retain M nodes then delete N nodes and continue the same till the end.

m = 2, n = 2
Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
Output : 1 -> 2 -> 5 -> 6 -> 9
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def print_list(head):
    while head:
        print(f" {head.val} -> ", end="")
        head = head.next
    print(f"None \n")


def arrange(head, m, n):
    curr = head

    while curr:
        for i in range(1, m):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return

        temp = curr.next
        for i in range(1, n+1):
            if temp is None:
                break
            temp = temp.next

        curr.next = temp
        curr = temp
    return head


def main():
    head = ListNode(9)
    for i in range(8, 0, -1):
        node = ListNode(i, head)
        head = node

    print_list(head)

    node = arrange(head, m=2, n=2)
    print_list(node)


if __name__ == '__main__':
    main()
