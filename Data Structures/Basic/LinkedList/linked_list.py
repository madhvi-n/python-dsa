"""
Linked List
Operations -> complexity

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        res = ""
        while itr:
            res += str(itr.data) + ' --> '
            itr = itr.next
        print(res)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        #If linked list is empty, node will become the head
        if self.head is None:
            self.head = Node(data, None)

        #Iterate through nodes. Loop will break for node whose next is None (last node)
        node = self.head
        while node.next:
            node = node.next

        #Insert the new node
        node.next = Node(data, None)


    def length(self):
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        node = self.head
        count = 0

        while node is not None:
            if count == index - 1:
                node = Node(data, node.next)
                node.next = node

            node = node.next
            count += 1

    def insert_values(self, arr):
        self.head = None
        for data in arr:
            self.insert_at_beginning(data)

    def remove_beginning(self):
        self.head = self.head.next

    def remove_end(self):
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        node = self.head
        count = 0

        while node is not None:
            if count == index - 1:
                node.next = node.next.next
                break

            node = node.next
            count += 1

    def insert_after_value(self, data_after, data):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_after, self.head.next)
            return

        node = self.head
        while node.next is not None:
            if node.data == data_after:
                node.next = Node(data, node.next)
                break
            node = node.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                break
            node = node.next

def main():
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(3)
    ll.print()
    ll.insert_at_end(8)
    ll.insert_at_end(9)
    ll.print()
    ll.remove_beginning()
    ll.print()
    ll.remove_end()
    ll.print()
    ll.remove_at(1)
    ll.print()


    ll2 = LinkedList()
    ll2.insert_values(["banana","mango","grapes","orange"])
    ll2.print()
    ll2.insert_after_value("mango","apple") # insert apple after mango
    ll2.print()
    ll2.remove_by_value("grapes") # remove orange from linked list
    ll2.print()
    ll2.remove_by_value("figs")
    ll2.print()
    ll2.remove_by_value("banana")
    ll2.remove_by_value("mango")
    ll2.remove_by_value("apple")
    ll2.remove_by_value("grapes")
    ll2.print()

if __name__ == '__main__':
    main()

"""
Output:

3 --> 1 --> 2 -->
3 --> 1 --> 2 --> 8 --> 9 -->
1 --> 2 --> 8 --> 9 -->
1 --> 2 --> 8 -->

orange --> grapes --> mango --> banana -->
orange --> grapes --> mango --> apple --> banana -->
orange --> mango --> apple --> banana -->
orange --> mango --> apple --> banana -->
orange -->
"""
