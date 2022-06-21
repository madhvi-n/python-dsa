"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque


def number_of_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def mark_current_island(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
            return

        grid[row][col] = "2"
        mark_current_island(row + 1, col)
        mark_current_island(row - 1, col)
        mark_current_island(row, col + 1)
        mark_current_island(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                mark_current_island(r, c)
                islands += 1
    return islands


# using bfs
def number_of_islands_ii(grid:list[list[str]]):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0
    
    def bfs(r, c):
        queue = deque()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            # convert popleft into pop, and it will remove the recently added element, making it iterative dfs
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                x, y = row + dr, col + dc

                if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(number_of_islands(grid[:]))
    print()

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(number_of_islands_ii(grid2))


if __name__ == '__main__':
    main()
