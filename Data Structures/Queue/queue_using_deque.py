from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, val):
        return self.data.appendleft(val)

    def dequeue(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def main():
    q = Queue()
    q.enqueue({
        'Company': 'Walmart',
        'timestamp': '15 April, 2021, 11:01 AM',
        'price': 131.10
    })
    q.enqueue({
        'Company': 'Walmart',
        'timestamp': '15 April, 2021, 11:02 AM',
        'price': 131.15
    })
    q.enqueue({
        'Company': 'Walmart',
        'timestamp': '15 April, 2021, 11:03 AM',
        'price': 131.25
    })

    print(q.data)
    q.dequeue()
    print(q.data)


if __name__ == '__main__':
    main()
