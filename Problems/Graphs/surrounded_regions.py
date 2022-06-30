"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board
are not flipped to 'X'. Any 'O' that is not on the border, and it is not connected to an 'O' on the border will
be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


def surrounded_regions(board: list[list[str]]):
    if not board: return board
    row, col = len(board), len(board[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    def dfs(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 'O' and (nx, ny) not in visited:
                visited.add((nx, ny))
                board[nx][ny] = 'G'
                dfs(nx, ny)

    for x in range(row):
        for y in range(col):
            if (x == 0 or x == row - 1 or y == 0 or y == col - 1) and board[x][y] == 'O' and (x, y) not in visited:
                board[x][y] = 'G'
                visited.add((x, y))
                dfs(x, y)

    for x in range(row):
        for y in range(col):
            if board[x][y] == 'O':
                board[x][y] = 'X'
            elif board[x][y] == 'G':
                board[x][y] = 'O'
    print(board)


def main():
    surrounded_regions([["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]])
    surrounded_regions([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
    surrounded_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])

    # [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    # [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    # [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]


if __name__ == '__main__':
    main()
