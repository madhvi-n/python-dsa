"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical).
Any cells outside the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that
make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.

Example 1:
grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1]
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0]
]

islands = [
    [X, X, X, 0, 0],
    [0, 0, X, X, X],
    [0, 1, 0, 0, 0],
    [X, 0, 1, 1, 0],
    [0, 1, 0, X, 0]
]
Output: 3
"""


# time complexity: O(n * m)
# every single cell of grid2 consisted an island exists in grid1
# for every single cell corresponding 1 in grid2, check simultaneously for the same in grid1
# Run dfs on grid2 and check the current row, col in grid1
def count_sub_islands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    num_sub_islands = 0
    rows = len(grid1)
    cols = len(grid1[0])

    def check_islands(row, col):

        if row < 0 or row >= rows or col < 0 or col >= cols or grid2[row][col] == 0:
            return True

        # If current cell in either of the grid is water, then the current cell cannot be sub-island.
        elif grid1[row][col] == 0 or grid2[row][col] == 0:
            return False

        # If the cell in both grids is land,change the value to mark it as visited or add it in visited set
        elif grid1[row][col] == 1 and grid2[row][col] == 1:
            grid2[row][col] = 0

            left = check_islands(row, col - 1)
            right = check_islands(row, col + 1)
            top = check_islands(row - 1, col)
            bottom = check_islands(row + 1, col)
            return left and right and top and bottom

    for row in range(len(grid2)):
        for col in range(len(grid2[row])):
            # If grid2 is land, and grid2 is a sub-island of grid 1
            if grid2[row][col] == 1 and check_islands(row, col):
                num_sub_islands += 1
    return num_sub_islands


def main():
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0]
    ]
    print(count_sub_islands(grid1, grid2))


if __name__ == '__main__':
    main()
