"""
Stack implementation using List
"""


class Stack(object):
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, val):
        self.items.append(val)
        self.top += 1
        pass

    def pop(self):
        self.items.pop()
        self.top -= 1

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[self.top]


def main():
    stack = Stack()
    stack.push(23)
    print(f"Top: {stack.top}")

    stack.push(19)
    print(f"Top: {stack.top}")

    stack.push(15)
    stack.pop()
    print(f"Stack Items: B {stack.items} T")
    print(f"Is stack empty? {stack.isEmpty()}")
    print(f"Top: {stack.top}")
    print(f"Peek: {stack.peek()}")


if __name__ == '__main__':
    main()
