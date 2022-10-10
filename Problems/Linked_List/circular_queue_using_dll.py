class ListNode:
    def __init__(self, val, next_node, prev):
        self.val = val
        self.next = next_node
        self.prev = prev


class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enqueue(self, val: int) -> bool:
        if self.is_full():
            return False
        curr = ListNode(val, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.size -= 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size += 1
        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.left.next.val

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.right.prev.val

    def is_empty(self) -> bool:
        return self.left.next == self.right

    def is_full(self) -> bool:
        return self.size == 0
