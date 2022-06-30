"""
Given a Directed Graph consisting of N vertices and M edges and a set of Edges[][],
the task is to check whether the graph contains a cycle or not using Topological sort.
"""
from collections import defaultdict


def has_cycle(n: int, edges: list[list[int]]):
    adjacency_list = defaultdict(list)

    for x, y in edges:
        adjacency_list[x].append(y)

    visited = [False] * n
    stack = []

    def dfs(vertex, visited, stack):
        visited[vertex] = True

        for v in adjacency_list[vertex]:
            if not visited[v]:
                dfs(v, visited, stack)
        stack.append(vertex)

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    print(len(stack) == n)


def main():
    has_cycle(4, [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]])


if __name__ == '__main__':
    main()
