"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from typing import List
from collections import deque


def generate(n: int) -> list:
    res = []
    queue = deque([('(', 1, 0)])

    while queue:
        curr, l, r = queue.popleft()

        if l == r == n:
            res.append(curr)

        if l < r or l > n or r > n:
            continue

        queue.append((curr + '(', l + 1, r))
        queue.append((curr + ')', l, r + 1))

    return res


def generate_parenthesis(n: int) -> list:
    # only add open parenthesis if open < n
    # only add closed parenthesis if closed < open
    # valid if open == closed == n

    stack = []
    res = []

    def backtrack(open_n, closed_n):
        if open_n == closed_n == n:
            res.append("".join(stack))
            return

        if open_n < n:
            stack.append("(")
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(")")
            backtrack(open_n, closed_n + 1)
            stack.pop()

    backtrack(0, 0)
    return res


def recursive_generate(n: int) -> list:
    res = []

    def recurse(n_open: int, n_close: int, curr: List[str]):
        if n_open == n_close == n:
            res.append("".join(curr))
            return

        if n_open < n:
            recurse(n_open + 1, n_close, curr + ["("])

        if n_open > n_close:
            recurse(n_open, n_close + 1, curr + [")"])

    recurse(0, 0, [])
    return res


def main():
    print(generate_parenthesis(3))
    print(generate(3))
    print(recursive_generate(3))


if __name__ == "__main__":
    main()
