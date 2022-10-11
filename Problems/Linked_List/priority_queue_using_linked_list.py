"""
Implement Priority Queue using Linked Lists.

push(): This function is used to insert a new data into the queue.
pop(): This function removes the element with the highest priority from the queue.
peek() / top(): This function is used to get the highest priority element in the queue
without removing it from the queue.

Algorithm -
PUSH(HEAD, DATA, PRIORITY):
Step 1: Create new node with DATA and PRIORITY
Step 2: Check if HEAD has lower priority. If true follow Steps 3-4 and end. Else goto Step 5.
Step 3: NEW -> NEXT = HEAD
Step 4: HEAD = NEW
Step 5: Set TEMP to head of the list
Step 6: While TEMP -> NEXT != NULL and TEMP -> NEXT -> PRIORITY > PRIORITY
Step 7: TEMP = TEMP -> NEXT
[END OF LOOP]
Step 8: NEW -> NEXT = TEMP -> NEXT
Step 9: TEMP -> NEXT = NEW
Step 10: End
POP(HEAD):

Step 1: Set the head of the list to the next node in the list. HEAD = HEAD -> NEXT.
Step 2: Free the node at the head of the list
Step 3: End
PEEK(HEAD):

Step 1: Return HEAD -> DATA
Step 2: End

Note: Considering low value, high priority
"""


class ListNode:
    def __init__(self, val=0, priority=0, next_node=None):
        self.val = val
        self.priority = priority
        self.next = next_node


class PriorityQueue:
    """PQ with low value, high priority"""
    def __init__(self):
        self.head = None

    def push(self, value: int, priority: int) -> None:
        """Adds node to the queue according to priority"""
        if self.is_empty():
            self.head = ListNode(value, priority)
            return
        else:
            if self.head.priority > priority:
                new_node = ListNode(value, priority)
                new_node.next = self.head
                self.head = new_node
                return
            else:
                temp = self.head
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                new_node = ListNode(value, priority)
                new_node.next = temp.next
                temp.next = new_node
                return

    def pop(self) -> None:
        """Removes node with high priority"""
        if self.is_empty():
            return
        self.head = self.head.next
        return

    def peek(self) -> int:
        """Returns value of high priority node"""
        if self.is_empty():
            return -1
        return self.head.val

    def is_empty(self) -> bool:
        return not self.head

    def traverse(self) -> None:
        """Returns the values of linked list"""
        if self.is_empty():
            print([])
            return
        temp = self.head
        result = []
        while temp:
            result.append(temp.val)
            temp = temp.next
        print(result)
        return


class PriorityQueue2:
    """PQ with high value, high priority"""
    def __init__(self):
        self.head = None

    def push(self, value: int, priority: int) -> None:
        """Adds node to the queue according to priority"""
        if self.is_empty():
            self.head = ListNode(value, priority)
            return
        else:
            if self.head.priority < priority:
                new_node = ListNode(value, priority)
                new_node.next = self.head
                self.head = new_node
                return
            else:
                temp = self.head
                while temp.next:
                    if priority >= temp.next.priority:
                        break
                    temp = temp.next
                new_node = ListNode(value, priority)
                new_node.next = temp.next
                temp.next = new_node
                return

    def pop(self) -> None:
        """Removes node with high priority"""
        if self.is_empty():
            return
        self.head = self.head.next
        return

    def peek(self) -> int:
        """Returns value of high priority node"""
        if self.is_empty():
            return -1
        return self.head.val

    def is_empty(self) -> bool:
        return not self.head

    def traverse(self) -> None:
        """Returns the values of linked list"""
        if self.is_empty():
            print([])
            return
        temp = self.head
        result = []
        while temp:
            result.append(temp.val)
            temp = temp.next
        print(result)
        return


def main():
    queue = PriorityQueue()
    queue.push(4, 1)
    queue.push(5, 2)
    queue.push(6, 3)
    queue.push(7, 0)
    queue.traverse()
    queue.pop()
    queue.traverse()

    queue2 = PriorityQueue2()
    queue2.push(4, 1)
    queue2.push(5, 2)
    queue2.push(6, 3)
    queue2.push(7, 0)
    queue2.traverse()
    queue2.pop()
    queue2.traverse()


if __name__ == '__main__':
    main()