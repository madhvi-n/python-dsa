"""
Max area of island
Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).

Example 1:

Input: grid = [[1,1,1,0],[0,0,1,0],[0,0,0,1]]
Output: 5
Explanation: The grid is-
1 1 1 0
0 0 1 0
0 0 0 1

Example 2:
Input: grid = [[0,1]]
Output: 1
Explanation: The grid is-
0 1
The largest region of 1's is colored in
orange.

Example 3:
Input: grid = [
    [0 1 1 1 1 1 1 1],
    [0 0 0 0 0 0 0 0],
    [0 0 0 1 0 0 0 1],
    [0 1 0 0 0 0 1 0],
    [1 1 1 0 0 1 0 0]
]
Output: 7
"""


# Max area of region connected horizontally and vertically
def max_area(grid: list[list[int]]):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    max_region = 0

    def mark_current_island(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
            return 0

        grid[row][col] = 2

        down = mark_current_island(row + 1, col)
        top = mark_current_island(row - 1, col)
        right = mark_current_island(row, col + 1)
        left = mark_current_island(row, col - 1)
        return top + down + right + left + 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                size = mark_current_island(r, c)
                max_region = max(size, max_region)
    return max_region


def largest_region(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    max_region = 0

    def get_biggest_region(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return 0
        if matrix[row][col] == 0 or matrix[row][col] == 2:
            return 0

        matrix[row][col] = 2
        size = 1
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
            new_row, new_col = row + r, col + c
            size += get_biggest_region(new_row, new_col)
        return size

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                curr_size = get_biggest_region(row, col)
                max_region = max(max_region, curr_size)

    return max_region


def main():
    grid = [
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 0]
    ]
    print(largest_region(grid))

    grid2 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    print(largest_region(grid2))


if __name__ == '__main__':
    main()
