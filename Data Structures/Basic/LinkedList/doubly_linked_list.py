"""
Doubly linked list
"""

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def last_node(self):
        """Returns last node of the doubly linked list"""
        node = self.head
        while node.next:
            node = node.next
        return node


    def length(self):
        """Returns length of the linked list"""
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def print_forward(self):
        """Prints nodes from front to rear"""
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        """Prints nodes from rear to front"""
        if self.head is None:
            print("Linked list is empty")
            return

        node = self.last_node()
        res = " "
        while node:
            res += str(node.data) + ' <-- '
            node = node.prev
        print(res)

    def insert_at_beginning(self, data):
        """Inserts node at the front"""
        if self.head == None:
            node = Node(data, None, self.head)
            self.head = node
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        """Inserts node at the rear"""
        if self.head is None:
            self.head = Node(data, None, None)
            return

        last = self.last_node()
        node = Node(data, last, None)


    def insert_at(self, index, data):
        """Inserts node at the given index"""
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        node = self.head
        while node:
            if count == index - 1:
                new_node = Node(data, node, node.next)
                if new_node.next:
                    new_node.next.prev = new_node
                node.next = new_node
                break

            node = node.next
            count += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data, node, None)

    def remove_at(self, index):
        count = 0
        node = self.head

        while node:
            if count == index - 1:
                node.next = node.next.next
                node.next.prev = node
            node = node.next
            count += 1
        pass


def main():
    dll = DoublyLinkedList()
    dll.insert_at_beginning("mango")
    dll.insert_at_beginning("grapes")
    dll.print_forward()

    dll.insert_at(1, "berries")
    dll.insert_at(3, "apple")
    dll.insert_at(2, "banana")
    dll.print_forward()

    dll.remove_at(1)
    dll.print_forward()


if __name__ == '__main__':
    main()
