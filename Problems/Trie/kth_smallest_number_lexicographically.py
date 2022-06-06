"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
so the second smallest number is 10.

Example 2:
Input: n = 1, k = 1
Output: 1
"""


class TrieNode:
    def __init__(self):
        self.children = dict.fromkeys(list('abcdefghijklmnopqrstuvwxyz'), None)
        self.word_end = None

    def __repr__(self):
        return str(self.children)


def insert(root, word):
    curr = root
    for char in word:
        curr = curr.children.setdefault(char, TrieNode())
    curr.word_end = word


def find_kth_number(n: int, k: int) -> int:
    if n == 1 and k == 1:
        return 1

    nums = [str(num) for num in range(1, n + 1)]
    result = []

    head = TrieNode()
    for num in nums:
        insert(head, num)

    curr = head

    def dfs(root, result):
        if root is None:
            return

        if root.word_end:
            result.append(root.word_end)

        for key, child in root.children.items():
            dfs(child, result)

    dfs(curr, result)
    # return result[k - 1] for smallest and result[n - k] for largest
    return result[k - 1]


def find_kth_smallest(n, k):
    cur = 1
    k = k - 1
    while k > 0:
        steps = calculate_steps(n, cur)
        if steps <= k:
            cur += 1
            k -= steps
        else:
            cur *= 10
            k -= 1
    return cur


def calculate_steps(n, cur):
    steps = 0
    n1, n2 = cur, cur + 1
    while n1 <= n:
        steps += min(n + 1, n2) - n1
        n1 *= 10
        n2 *= 10
    return steps


def main():
    print(find_kth_number(10, 2))
    print(find_kth_number(15, 3))
    print(find_kth_smallest(30, 5))
    print(find_kth_smallest(100, 9))


if __name__ == '__main__':
    main()
