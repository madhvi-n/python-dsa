"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network
where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers
directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
"""
from collections import defaultdict


# find bridges using tarjan's algorithm
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    graph = defaultdict(list)

    for src, dest in connections:
        graph[src].append(dest)
        graph[dest].append(src)

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    visited = [False] * n
    time = 0
    bridges = []

    def dfs(src, visited, disc, low, parent, time):
        visited[src] = True
        disc[src] = low[src] = time
        time += 1

        for adjacent in graph[src]:
            if not visited[adjacent]:
                parent[adjacent] = src
                dfs(adjacent, visited, disc, low, parent, time)
                low[src] = min(low[src], low[adjacent])

                if low[adjacent] > disc[src]:
                    bridges.append([src, adjacent])
            
            elif adjacent != parent[src]:
                low[src] = min(low[src], disc[adjacent])

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, disc, low, parent, time)
    return bridges


def main():
    print(critical_connections(8, [[0, 1], [0, 2], [1, 2], [0, 3], [3, 4], [1, 5], [5, 6], [5, 7], [6, 7]]))
    print(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
    print(critical_connections(2, [[0, 1]]))


if __name__ == '__main__':
    main()
