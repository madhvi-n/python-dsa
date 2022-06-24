"""
Given a 2D grid consists of 0s (land) and 1s (water).
An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally
(all left, top, right, bottom) surrounded by 1s. Return the number of closed islands.

Example 1:
Input: grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]
]
Output: 2

Example 2:
Input: grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0]
]
Output: 1

Example 3:
Input: grid = [[1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1]
            ]
Output: 2
"""


def closed_islands(grid: list[list[int]]):
    rows = len(grid)
    cols = len(grid[0])

    def search(grid, row, col):
        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0:
            grid[row][col] = 2
            search(grid, row + 1, col)
            search(grid, row - 1, col)
            search(grid, row, col + 1)
            search(grid, row, col - 1)

    for r in range(rows):
        search(grid, r, 0)
        search(grid, r, cols - 1)

    for c in range(cols):
        search(grid, 0, c)
        search(grid, rows - 1, c)

    res = 0
    for row in range(1, rows):
        for column in range(1, cols):
            if grid[row][column] == 0:
                res += 1
                search(grid, row, column)
    return res


def number_of_closed_islands(grid: list[list[int]]):
    if grid is None:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    closed_islands = 0
    seen = set()

    def check_closed_island(row, col):
        if row < 0 or row == rows or col < 0 or col == cols:
            return False

        if grid[row][col] == 1:
            return True

        grid[row][col] = 1
        seen.add((row, col))
        top = check_closed_island(row - 1, col)
        bottom = check_closed_island(row + 1, col)
        left = check_closed_island(row, col - 1)
        right = check_closed_island(row, col + 1)
        return top and bottom and left and right

    for row in range(1, rows - 1):
        for column in range(1, cols - 1):
            if grid[row][column] == 0 and (row, column) not in seen:
                if check_closed_island(row, column):
                    closed_islands += 1
    return closed_islands


def main():
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]
    print(closed_islands(grid))

    grid2 = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    print(number_of_closed_islands(grid2))


if __name__ == '__main__':
    main()
