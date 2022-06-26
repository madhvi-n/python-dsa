"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer
directly or indirectly through the network.
You are given an initial computer network connections. You can extract certain cables between two directly connected
computers, and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected.
If it is not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
"""
from collections import defaultdict


def make_connected(n: int, connections: list[list[int]]) -> int:
    graph = defaultdict(list)
    visited = [False] * n
    components = 0
    edges = len(connections)

    # if edges are less than of required edges for a connected graph, return -1
    if edges < n - 1:
        return -1

    # create adjacency list for graph
    for src, dest in connections:
        graph[src].append(dest)
        graph[dest].append(src)

    def dfs(src, visited):
        visited[src] = True
        for adjacent in graph[src]:
            if not visited[adjacent]:
                dfs(adjacent, visited)

    # find no of components using dfs
    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            components += 1

    # calculate redundant edges using formula
    redundant_edges = edges - ((n - 1) - (components - 1))
    if redundant_edges >= components - 1:
        return components - 1
    return -1


def main():
    print(make_connected(12, [[1, 5], [1, 7], [1, 2], [1, 4], [3, 7], [4, 7], [3, 5], [0, 6], [0, 1], [0, 4], [2, 6],
                              [0, 3], [0, 2]]))
    print(make_connected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))


if __name__ == '__main__':
    main()
