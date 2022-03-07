"""
Stack implementation using List
"""

class Stack(object):
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]


def main():
    stack = Stack()
    stack.push(23)
    print(f"Top: {stack.peek()}")

    stack.push(19)
    print(f"Top: {stack.peek()}")

    stack.push(15)
    stack.pop()

    print(f"Is stack empty? {stack.is_empty()}")
    print(f"Peek: {stack.peek()}")


if __name__ == '__main__':
    main()


"""
Output:
Top: 23
Top: 19
Stack Items: B [23, 19] T
Is stack empty? False
Top: 15
"""
