"""
Given a non-empty 2D array grid of 0’s and 1’s, an island is a group of 1’s (representing land) connected 4-directionally
(horizontal or vertical.) An island is a group of 1s that are grouped together whose perimeter is surrounded by water.
Find the number of completely surrounded islands.
"""


def surrounded_islands(matrix: list[list]):
    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0

    def check_island(row, col):
        if row < 0 or col < 0 or row >= rows or col >= rows:
            return False

        if matrix[row][col] == 0:
            return True

        matrix[row][col] = 0

        a = check_island(row + 1, col)
        b = check_island(row - 1, col)
        c = check_island(row, col + 1)
        d = check_island(row, col - 1)

        return a and b and c and d

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                if check_island(row, col):
                    islands += 1
    return islands


def main():
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(surrounded_islands(matrix))


if __name__ == '__main__':
    main()
