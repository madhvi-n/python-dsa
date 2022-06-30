"""
Given n nodes labelled from 0 to n - 1 and a list of undirected edges, write a function to check whether these edges
make a valid tree. Assume there are no duplicate edges.

Example 1:
Input: n = 5,  edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: True
"""
from collections import defaultdict, deque


def valid_tree(n: int, edges: list[list[int]]):
    if not n:
        return True

    graph = defaultdict(list)

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = set()

    def dfs(src, prev):
        if src in visited:
            return False

        visited.add(src)
        for adjacent in graph[src]:
            if adjacent == prev:
                continue
            if not dfs(adjacent, src):
                return False
        return True

    return dfs(0, -1) and n == len(visited)


def valid_tree_ii(n: int, edges: list[list]):
    if not n:
        return True

    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = set()
    queue = deque([0])

    while queue:
        node = queue.popleft()
        visited.add(node)

        for adjacent in graph[node]:
            if adjacent not in visited:
                queue.append(adjacent)
    return len(visited) == n


def main():
    print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print(valid_tree_ii(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


if __name__ == '__main__':
    main()
