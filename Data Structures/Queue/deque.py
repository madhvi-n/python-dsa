"""
Deque or Double ended queue implementation using List
"""

class Deque(object):
    def __init__(self, max_size):
        self.deque = []
        self.max_size = max_size
        self.front = -1
        self.rear = 0

    def add_front(self, val):
        if self.front < 1:
            self.front = self.max_size - 1
        self.front -= 1
        self.deque.insert(self.front, val)

    def add_rear(self, val):
        if self.isFull():
            self.rear = 0
        self.rear += 1
        self.deque.insert(self.rear, val)

    def remove_front(self):
        if self.isEmpty():
            return 'Overflow condition'

        if len(self.deque) == 1:
            self.front = -1
            self.rear = -1
        elif self.front == self.max_size - 1:
            self.front = 0
        else:
            self.front += 1

    def remove_rear(self):
        if self.isEmpty():
            return 'Underflow condition'

        if len(self.deque) == 1:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.max_size - 1
        else:
            self.rear -= 1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.max_size == len(self.deque)
        # return self.front == self.rear + 1


def main():
    deque = Deque(max_size=5)
    print(f"Deque: {deque.deque}")
    print(f"Front: {deque.front}, Rear: {deque.rear}")

    deque.add_front(1)
    print(f"add_front(1) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.add_front(2)
    print(f"add_front(2) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.add_rear(3)
    print(f"add_rear(3) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.add_rear(4)
    print(f"add_rear(4) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.add_rear(5)
    print(f"add_rear(5) -> Front: {deque.front}, Rear: {deque.rear}")

    print(f"Deque: {deque.deque}")
    print(f"Is deque full? {deque.is_full()}")



if __name__ == '__main__':
    main()


"""
Output:
Deque: []
Front: -1, Rear: 0
add_front(1) -> Front: -2, Rear: 0
add_front(2) -> Front: -1, Rear: 0
add_rear(3) -> Front: -1, Rear: 1
add_rear(4) -> Front: -1, Rear: 2
add_rear(5) -> Front: -1, Rear: 3
Deque: [2, 3, 4, 5, 1]
Is deque full? True
"""
