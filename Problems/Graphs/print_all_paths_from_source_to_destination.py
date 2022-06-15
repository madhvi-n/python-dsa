"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node
n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""
from collections import defaultdict


def all_paths_source_target(graph: list[list[int]]):
    if graph is None:
        return []

    adjacency_list = defaultdict(list)

    for index in range(len(graph)):
        adjacency_list[index] += graph[index]

    visited = [False] * len(graph)
    path = []
    result = []

    def dfs(source, destination, visited, path):
        visited[source] = True
        path.append(source)

        if source == destination:
            result.append(path[:])
        else:
            for v in adjacency_list[source]:
                if not visited[v]:
                    dfs(v, destination, visited, path)
        path.pop()
        visited[source] = False

    dfs(0, len(graph) - 1, visited, path)
    print(result)


def all_paths_from_source(graph: list[list[int]]):
    ...


def main():
    all_paths_source_target([[1, 2], [3], [3], []])
    all_paths_source_target([[4, 3, 1], [3, 2, 4], [3], [4], []])


if __name__ == '__main__':
    main()
