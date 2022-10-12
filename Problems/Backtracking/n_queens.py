"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""


def n_queens(n: int) -> list[list[str]]:
    column_set = set()
    positive_diagonal = set()
    negative_diagonal = set()
    result = []
    board = [["." for _ in range(n)] for _ in range(n)]

    def backtrack(r: int):
        if r == n:
            copy = [" ".join(row) for row in board]
            result.append(copy)
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
    return result


def main():
    print(n_queens(4))


if __name__ == '__main__':
    main()
