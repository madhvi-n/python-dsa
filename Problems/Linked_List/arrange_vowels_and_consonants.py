"""
https://practice.geeksforgeeks.org/problems/arrange-consonants-and-vowels/

Given a singly linked list of size N containing only English Alphabets. Your task is to complete the function arrangeC&V(), that arranges the consonants and vowel nodes of the list it in such a way that all the vowels nodes come before the consonants while maintaining the order of their arrival.

Input:
The function takes a single argument as input, the reference pointer to the head of the linked list. There will be T test cases and for each test case the function will be called separately.

Output:
For each test case output a single line containing space separated elements of the list.


Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
a e g h i m
q r t

Output:
a e i g h m
q r t
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print()


def arrange(head):
    if head is None:
        return None

    vowels_char = ['a', 'e', 'i', 'o', 'u']
    vowel, consonant = None, None
    start, end = vowel, consonant

    while head:
        if head.val in vowels_char:
            if vowel is None:
                vowel = head
                start = vowel
            else:
                vowel.next = head
                vowel = vowel.next
        else:
            if consonant is None:
                consonant = head
                end = consonant
            else:
                consonant.next = head
                consonant = consonant.next

    if start is None:
        return end

    vowel.next = end

    return start


def main():
    head = ListNode('a')
    head.next = ListNode('o')
    head.next.next = ListNode('h')
    head.next.next.next = ListNode('i')
    head.next.next.next.next = ListNode('m')

    print_list(head)

    node = arrange(head)
    print_list(node)


if __name__ == '__main__':
    main()
