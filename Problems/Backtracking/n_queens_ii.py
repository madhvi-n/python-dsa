"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
"""


def n_queens(n: int) -> list[list[str]]:
    column_set = set()
    positive_diagonal = set()
    negative_diagonal = set()
    board = [["." for _ in range(n)] for _ in range(n)]
    count = 0

    def backtrack(r: int):
        nonlocal count
        if r == n:
            count += 1
            return

        for c in range(n):
            if c in column_set or (r + c) in positive_diagonal or \
                    (r - c) in negative_diagonal:
                continue
            column_set.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)

            column_set.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return count


def main():
    print(n_queens(4))
    print(n_queens(8))


if __name__ == '__main__':
    main()
