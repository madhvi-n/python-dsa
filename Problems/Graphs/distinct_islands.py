"""
Given a non-empty 2D array grid of 0’s and 1’s, an island is a group of 1’s (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be
translated (and not rotated or reflected) to equal the other.
"""


def distinct_islands(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0

    if rows == 0:
        return 0

    def mark_islands(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or matrix[row][col] == "0":
            return

        matrix[row][col] = "0"
        mark_islands(row + 1, col)
        mark_islands(row - 1, col)
        mark_islands(row, col + 1)
        mark_islands(row, col - 1)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                islands += 1
            mark_islands(row, col)
    return islands


def main():
    matrix = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(distinct_islands(matrix))


if __name__ == '__main__':
    main()
