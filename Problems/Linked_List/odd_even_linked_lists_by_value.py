def odd_even_list(head):
    if head is None:
        return None

    odd, even = ListNode(), ListNode()
    oddTail, evenTail = odd, even

    while head:
        if count % 2 != 0:
            oddTail.next = head
            oddTail = oddTail.next
        else:
            evenTail.next = head
            evenTail = evenTail.next
        head = head.next

    oddTail.next = even.next
    evenTail.next = None

    return odd.next


def odd_even_list_by_index(head):
    if head is None:
            return None

    odd, even = ListNode(), ListNode()
    oddTail, evenTail = odd, even

    count = 0
    while head:
        if count % 2 == 0:
            evenTail.next = head
            evenTail = evenTail.next
        else:
            oddTail.next = head
            oddTail = oddTail.next
        head = head.next
        count += 1

    evenTail.next = odd.next
    oddTail.next = None

    return even.next
