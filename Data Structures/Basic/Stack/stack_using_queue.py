from queue import LifoQueue


class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, val):
        self.stack.put(val)

    def pop(self):
        self.stack.get()

    def is_full(self):
        return self.stack.full()

    def is_empty(self):
        return self.stack.empty()

    def size(self):
        return self.stack.qsize()


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.is_empty())
    print(s.size())


if __name__ == '__main__':
    main()
