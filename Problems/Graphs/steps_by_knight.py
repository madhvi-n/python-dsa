"""
Given a square chessboard, the initial position of Knight and position of a target.
Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3

Explanation:
[                                   [
    [0, 0, 0, 0, 0, 0],                 [0, X, 0, 0, 0, X],
    [0, 0, 0, K, 0, 0],                 [0, 0, 0, K, 0, 0],
    [0, 0, 0, 0, 0, 0],     =>          [0, X, 0, 0, 0, X],
    [0, 0, 0, 0, 0, 0],                 [0, 0, X, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],                 [0, 0, 2, 0, 0, 0],
    [T, 0, 0, 0, 0, 0],                 [3, 0, 0, 0, 0, 0]
]                                   ]
Knight takes 3 step to reach from
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
"""
from collections import deque


def min_steps_to_reach_target(n, knight_pos, target_pos):
    queue = deque([knight_pos])
    visited = set()
    path = dict()
    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    visited.add(knight_pos)

    while queue:
        node = queue.popleft()
        if node == target_pos:
            count = 0
            curr = target_pos

            while curr != knight_pos:
                count += 1
                curr = path[curr]
            return count

        for dr, dc in moves:
            row, col = node
            x, y = row + dr, col + dc

            # since it's not 0-based indexing
            if x in range(1, n + 1) and y in range(1, n + 1) and (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))
                path[(x, y)] = node
    return -1


def main():
    print(min_steps_to_reach_target(6, (4, 5), (1, 1)))


if __name__ == '__main__':
    main()
