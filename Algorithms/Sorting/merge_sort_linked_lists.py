"""
Merge sort on LinkedList
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def last_node(self):
        node = self.head
        while node:
            node = node.next
        return node

    def insert_values(self, values):
        for val in values:
            node = ListNode(val, self.head)
            self.head = node


def merge_linked_list() -> LinkedList:
    pass


def main():
    l1 = LinkedList()
    l1.insert_values([4, 1, 2, 3, 5, 8])

    print(l1)


if __name__ == '__main__':
    main()
