"""
Deque or Double ended queue implementation using List
"""

class Deque(object):
    def __init__(self, max_size):
        self.deque = []
        self.max_size = max_size
        self.front = -1
        self.rear = 0

    def addFront(self, val):
        if self.front < 1:
            self.front = self.max_size - 1
        self.front -= 1
        self.deque.insert(self.front, val)

    def addRear(self, val):
        if self.isFull():
            self.rear = 0
        self.rear += 1
        self.deque.insert(self.rear, val)

    def removeFront(self):
        if self.isEmpty():
            return 'Overflow condition'

        if len(self.deque) == 1:
            self.front = -1
            self.rear = -1
        elif self.front == self.max_size - 1:
            self.front = 0
        else:
            self.front += 1

    def removeRear(self):
        if self.isEmpty():
            return 'Underflow condition'

        if len(self.deque) == 1:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.max_size - 1
        else:
            self.rear -= 1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.max_size == len(self.deque)
        # return self.front == self.rear + 1


def main():
    deque = Deque(max_size=5)
    print(f"Deque: {deque.deque}")
    print(f"Front: {deque.front}, Rear: {deque.rear}")

    deque.addFront(1)
    print(f"addFront(1) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.addFront(2)
    print(f"addFront(2) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.addRear(3)
    print(f"addRear(3) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.addRear(4)
    print(f"addRear(4) -> Front: {deque.front}, Rear: {deque.rear}")

    deque.addRear(5)
    print(f"addRear(5) -> Front: {deque.front}, Rear: {deque.rear}")

    print(f"Deque: {deque.deque}")
    print(f"Is deque full? {deque.isFull()}")



if __name__ == '__main__':
    main()


"""
Output:
Deque: []
Front: -1, Rear: 0
addFront(1) -> Front: -2, Rear: 0
addFront(2) -> Front: -1, Rear: 0
addRear(3) -> Front: -1, Rear: 1
addRear(4) -> Front: -1, Rear: 2
addRear(5) -> Front: -1, Rear: 3
Deque: [2, 3, 4, 5, 1]
Is deque full? True
"""
