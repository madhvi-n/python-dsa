"""
Queue implementation using List
"""

class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, val):
        self.queue.append(val)
        if len(self.queue) == 1:
            self.front += 1
            self.rear += 1
        else:
            self.rear +=1

    def dequeue(self):
        self.queue.pop(0)
        self.front += 1
        if len(self.queue) == 0:
            self.front = -1
            self.rear = -1

    def isEmpty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        return "Queue is empty"
        

def main():
    queue = Queue()
    print(f"Initial: {queue.queue}")
    print(f"Front: {queue.front}")
    print(f"Rear: {queue.rear}")

    print(f"Enqueue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"Current: {queue.queue}")
    print(f"Front: {queue.front}")
    print(f"Rear: {queue.rear}")

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(f"Dequeue: {queue.queue}")
    print(f"Front: {queue.front}")
    print(f"Rear: {queue.rear}")

    queue.dequeue()
    print(f"Queue: {queue.queue}")
    print(f"Front: {queue.front}")
    print(f"Rear: {queue.rear}")
    print(f"Is queue empty?: {queue.isEmpty()}")


if __name__ == '__main__':
    main()


"""
Output:
Initial: []
Front: -1
Rear: -1
Enqueue
Current: [1, 2, 3, 4, 5]
Front: 0
Rear: 4
Dequeue: [5]
Front: 4
Rear: 4
Queue: []
Front: -1
Rear: -1
Is queue empty?: True
"""
