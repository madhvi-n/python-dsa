"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], word = 'ABCCED'
Output: true
"""


def word_search(board: list[list], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited_path = set()

    def dfs(index, row, col):
        if index == len(word):
            return True

        if row < 0 or col < 0 or \
                row >= rows or col >= cols or \
                word[index] != board[row][col] or \
                (row, col) in visited_path:
            return False

        visited_path.add((row, col))

        res = (
            dfs(row + 1, col, index + 1),
            dfs(row - 1, col, index + 1),
            dfs(row, col + 1, index + 1),
            dfs(row, col - 1, index + 1)
        )

        visited_path.remove((row, col))

        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


# Time complexity O(rows * cols * dfs) => O(n * m * 4 ^ word length)


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(word_search(board, 'ABCCED'))
    print(word_search(board, 'SEE'))
    print(word_search(board, 'SAD'))
    print(word_search(board, 'FACE'))


if __name__ == '__main__':
    main()
