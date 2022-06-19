"""
Find strongly connected components
"""
from collections import defaultdict


def is_scc(n: int, edges: list[list]):
    edges = edges
    adjacency_list = defaultdict(list)
    stack = []
    visited = [False] * n
    revisit = [False] * n

    for x, y in edges:
        adjacency_list[x].append(y)

    def dfs(vertex, visited, stack):
        visited[vertex] = True
        for node in adjacency_list[vertex]:
            if not visited[node]:
                dfs(node, visited, stack)
        stack.append(vertex)

    def dfs2(vertex, visited):
        visited[vertex] = True
        for node in adjacency_list[vertex]:
            if not visited[node]:
                dfs2(node, visited)

    def transpose_graph():
        adjacency_list.clear()
        for x, y in edges:
            adjacency_list[y].append(x)

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    if any(visit == False for visit in visited):
        return False

    transpose_graph()

    while stack:
        curr = stack.pop()
        if not revisit[curr]:
            dfs2(curr, revisit)

    if any(visit == False for visit in revisit):
        return False
    return True


def find_scc(n: int, edges: list[list]):
    edges = edges
    adjacency_list = defaultdict(list)
    stack = []
    visited = [False] * n
    revisit = [False] * n

    for x, y in edges:
        adjacency_list[x].append(y)

    def dfs(vertex, visited, stack):
        visited[vertex] = True
        for node in adjacency_list[vertex]:
            if not visited[node]:
                dfs(node, visited, stack)
        stack.append(vertex)

    def dfs2(vertex, visited):
        print(vertex, end=" ")
        visited[vertex] = True
        for node in adjacency_list[vertex]:
            if not visited[node]:
                dfs2(node, visited)
        print()

    def transpose_graph():
        adjacency_list.clear()
        for x, y in edges:
            adjacency_list[y].append(x)

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    transpose_graph()

    while stack:
        curr = stack.pop()
        if not revisit[curr]:
            dfs2(curr, revisit)


def main():
    edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [4, 7], [5, 6], [6, 4], [6, 7]]
    find_scc(8, edges)
    print()
    print(is_scc(8, edges))


if __name__ == '__main__':
    main()
