class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, val):
        if self.head is None:
            self.head = Node(val)

        node = Node(val, self.head)
        self.head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        removed_value = self.head.val
        self.head = self.head.next
        self._size -= 1
        return removed_value

    def is_empty(self):
        return self._size == 0

    def peek(self):
        return self.head.val

    def size(self):
        return self._size


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.is_empty())
    print(s.size())


if __name__ == '__main__':
    main()
