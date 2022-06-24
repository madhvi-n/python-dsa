from collections import defaultdict


def find_bridges(n: int, edges: list[list[int]]):
    graph = defaultdict(list)
    time = 0

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    disc = [-1] * n
    low = [-1] * n
    visited = [False] * n
    parent = [-1] * n
    bridges = []

    def dfs(src, visited, disc, low, parent, time):
        visited[src] = True
        disc[src] = time
        low[src] = time
        time += 1

        for adjacent in graph[src]:
            if not visited[adjacent]:
                parent[adjacent] = src
                dfs(adjacent, visited, disc, low, parent, time)
                low[src] = min(low[src], low[adjacent])

                # The condition for an edge (u, v) to be a bridge is, low[v] > disc[u].
                if low[adjacent] > disc[src]:
                    bridges.append([src, adjacent])

            elif adjacent != parent[src]:
                low[src] = min(low[src], disc[adjacent])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, visited, disc, low, parent, time)

    print(bridges)


def main():
    find_bridges(5, [[0, 2], [0, 3], [0, 1], [1, 2], [3, 4]])
    find_bridges(7, [[0, 2], [0, 1], [1, 2], [1, 6], [1, 3], [1, 4], [3, 5], [4, 5]])
    find_bridges(4, [[0, 1], [1, 2], [2, 3]])


if __name__ == '__main__':
    main()
