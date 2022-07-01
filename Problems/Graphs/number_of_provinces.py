"""
There are n cities. Some of them are connected, while some are not.
If city 'a' is connected directly with city 'b', and city 'b' is connected directly with city 'c',
then city 'a' is connected indirectly with city 'c'.

A province is a group of directly or indirectly connected cities and no other cities outside the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
Output: 2
Example 2:

Input: isConnected = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
Output: 3
"""
from collections import defaultdict


# Time complexity: O(n * n)
def provinces(matrix: list[list[int]]):
    n = len(matrix)
    visited = set()

    def dfs(source):
        for adjacent in range(n):
            if matrix[source][adjacent] == 1 and adjacent not in visited:
                visited.add(adjacent)
                dfs(adjacent)

    ans = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            ans += 1
    return ans


# Union find
def number_of_provinces(matrix: list[list[int]]):
    ...


def main():
    print(provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    print(provinces([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))


if __name__ == '__main__':
    main()
