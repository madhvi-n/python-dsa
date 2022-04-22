"""
Doubly Linked List
"""


class Node:
    def __init__(self, val, next_node=None, prev=None):
        self.val = val
        self.next = next_node
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self) -> None:
        node = self.head
        while node:
            print(f"{node.val} ->", end="")
        print()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp.val

    def insert_at_beginning(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.insert_at_beginning(val)
            return
        temp = self.head
        while temp and temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        self.size += 1

    def insert_at(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.insert_at_beginning(val)
            return
        if index == self.size:
            self.insert_at_end(val)
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next

        new_node = Node(val)
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
        self.size += 1

    def delete_head(self) -> None:
        if self.size is None:
            return
        if self.size == 1:
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None

        self.size -= 1

    def delete_tail(self) -> None:
        if self.size is None:
            return

        temp = self.head
        while temp and temp.next:
            temp = temp.next

        prev_node = temp.prev
        temp.prev = None
        prev_node.next = None
        self.size -= 1

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.delete_head()
            return

        if index == (self.size - 1):
            self.delete_tail()
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next

        prev_node = temp.prev
        after_node = temp.next
        prev_node.next = after_node
        after_node.prev = prev_node
        temp.next = None
        temp.prev = None
        self.size -= 1


def main():
    dll = DoublyLinkedList()
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    dll.print_list()

    dll.insert_at(1, 5)
    dll.insert_at(3, 6)
    dll.insert_at(2, 7)
    dll.print_list()

    dll.remove_at(1)
    dll.print_list()


if __name__ == '__main__':
    main()
