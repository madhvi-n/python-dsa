# Streamlining the push operation to O(1) and trading off pop to O(n).

from collections import deque


class Stack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0


# Streamlining pop to O(1) and trading off push to O(n).
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q2.append(x)
        self._top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        result = self.q1.popleft()
        if self.q1:
            self._top = self.q1[0]
        return result

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0


class MyStack2:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Insert an item into the stack
    def add(self, data):
        # Move all elements from the first queue to the second queue
        while len(self.q1):
            self.q2.append(self.q1.pop())

        # Push the given item into the first queue
        self.q1.append(data)

        # Move all elements back to the first queue from the second queue
        while len(self.q2):
            self.q1.append(self.q2.pop())

    # Remove the top item from the stack
    def pop(self):
        # if the first queue is empty
        if not self.q1:
            raise Exception("Stack is empty")
        # return the front item from the first queue
        front = self.q1.popleft()
        return front


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.empty())
    print(s.top())


if __name__ == '__main__':
    main()
