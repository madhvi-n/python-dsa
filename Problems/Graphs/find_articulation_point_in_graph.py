"""
Simple Approach: DFS
Time complexity: O(V * (V + E))
For each node, remove the node and adjacent edges
Perform dfs and check if all nodes are visited.
If yes, the removed node was not an articulation point, else append it to result.
Print result
"""
from collections import defaultdict


def find_articulation_points(n: int, edges: list[list[int]]):
    graph = defaultdict(list)
    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    articulation_points = [False] * n
    time = 0

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    def dfs(src, visited, articulation_points, parent, low, disc, time):
        children = 0
        visited[src] = True
        disc[src] = time
        low[src] = time
        time += 1

        for adjacent in graph[src]:
            if not visited[adjacent]:
                parent[adjacent] = src
                children += 1
                dfs(adjacent, visited, articulation_points, parent, low, disc, time)
                low[src] = min(low[src], low[adjacent])

                if parent[src] == -1 and children > 1:
                    articulation_points[src] = True

                if parent[src] != -1 and low[adjacent] >= disc[src]:
                    articulation_points[src] = True

            elif adjacent != parent[src]:
                low[src] = min(low[src], disc[adjacent])

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, articulation_points, parent, low, disc, time)

    res = [i for i, v in enumerate(articulation_points) if v]
    return res


def main():
    g1 = find_articulation_points(5, [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]])
    print(f"Articulation points in first graph: {g1}")

    g2 = find_articulation_points(4, [[0, 1], [1, 2], [2, 3]])
    print(f"Articulation points in second graph: {g2}")

    g3 = find_articulation_points(7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]])
    print(f"Articulation points in third graph: {g3}")


if __name__ == '__main__':
    main()
