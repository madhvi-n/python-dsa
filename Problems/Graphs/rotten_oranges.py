"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1]
(up, down, left and right) in unit time.

Example 1:
Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and
(2,1) in unit time.
"""
from collections import deque


def rotten_oranges(grid: list[list[int]]) -> None:
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh += 1

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    levels = 0

    while queue:
        levels += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                    fresh -= 1
                    grid[r][c] = 2
                    queue.append((r, c))
    return -1 if fresh != 0 else max(levels - 1, 0)


def rotten_oranges_ii(grid: list[list[int]]) -> None:
    rotten = set()
    row, cols = len(grid), len(grid[0])
    fresh = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                rotten.add((i, j))
            if grid[i][j] == 1:
                fresh += 1
    levels = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while rotten:
        levels += 1
        temp = set()
        for (x, y) in rotten:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    temp.add((nx, ny))
        rotten = temp
    return max(levels - 1, 0) if fresh == 0 else -1


def main():
    print(rotten_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(rotten_oranges([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))
    print(rotten_oranges([[0, 2]]))
    print(rotten_oranges([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]))
    print(rotten_oranges_ii([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]))


if __name__ == '__main__':
    main()
