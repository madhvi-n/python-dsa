from collections import deque


class Stack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.empty())
    print(s.top())


if __name__ == '__main__':
    main()
