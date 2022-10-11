"""
Given Nodes with their priority, implement a priority queue using doubly linked list.

push(): This function is used to insert a new data into the queue.
pop(): This function removes the element with the lowest priority value from the queue.
peek() / top(): This function is used to get the lowest priority element in the queue without
removing it from the queue.
"""


class ListNode:
    def __init__(self, val=0, priority=0, prev=None, next_node=None):
        self.val = val
        self.priority = priority
        self.prev = prev
        self.next = next_node


class PriorityQueue:
    """PQ with low value, high priority"""

    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, value: int, priority: int):
        new_node = ListNode(value, priority)
        if self.front is None:  # if list is empty
            self.front = new_node
            self.rear = new_node
        else:
            # if priority is less than or equal to front node's priority
            if self.front.priority >= priority:
                new_node.next = self.front
                self.front.prev = new_node.next
                self.front = new_node

            elif priority > self.rear.priority:  # if priority is more than rear node's priority
                new_node.next = None
                self.rear.next = new_node
                new_node.prev = self.rear.next
                self.rear = new_node

            else:  # find position to insert the new node
                temp = self.front.next

                while temp.next and temp.priority > priority:
                    temp = temp.next

                temp.prev.next = new_node
                new_node.next = temp.prev
                new_node.prev = temp.prev.next
                temp.prev = new_node.next

    def pop(self):
        if self.is_empty():
            return
        self.front = self.front.next
        self.front.prev = None

    def peek(self):
        if self.is_empty():
            print(-1)
            return
        print(self.front.val)

    def is_empty(self):
        return self.front is None and self.rear is None

    def traverse(self):
        if self.is_empty():
            print([])
            return

        temp = self.front
        result = []
        while temp:
            result.append(temp.val)
            temp = temp.next
        print(result)


def main():
    queue = PriorityQueue()
    queue.push(2, 3)
    queue.push(3, 4)
    queue.push(4, 5)
    queue.push(5, 6)
    queue.push(6, 7)
    queue.push(1, 2)
    queue.traverse()
    queue.pop()
    queue.traverse()
    queue.peek()


if __name__ == '__main__':
    main()
