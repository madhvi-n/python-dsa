"""
Given a directed acyclic graph (DAG), print all its topological orderings.

Algorithm:
The idea remains similar to Kahn’s topological sort, where we find vertices with no incoming edges and removing all
outgoing edges from these vertices.
We build all possible orderings from left to right, where the vertices with in-degree zero become candidates for
the next vertex. We can do this using backtracking, where the graph state is restored after processing the selected vertex.
"""
from collections import defaultdict


# Time complexity: Exponential
def topological_orders(n: int, edges: list[list[int]]):
    # Create an adjancecy list and store indegree of each vertex
    graph = defaultdict(list)
    indegree = [0] * n

    visited = [False] * n
    path = []
    result = []

    for src, dest in edges:
        graph[src].append(dest)
        indegree[dest] += 1

    def dfs(visited, path):
        # for every vertex
        for v in range(n):

            # proceed if indegree is 0 and vertex has not been visited
            if indegree[v] == 0 and not visited[v]:

                # for every adjacent u of vertex v, reduce indegree by 1
                for u in graph[v]:
                    indegree[u] -= 1

                # include current vertex in path and mark it as visited
                path.append(v)
                visited[v] = True

                # call dfs recursively for other vertices
                dfs(visited, path)

                # backtracking: reset indegree for the current node
                for u in graph[v]:
                    indegree[u] += 1

                # remove current vertex from path and mark it as unvisited
                path.pop()
                visited[v] = False

        # append a copy of path to result if length of path equals to no of vertices
        if len(path) == n:
            result.append(path[:])

    dfs(visited, path)
    return result


def main():
    print(topological_orders(8, [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]))


if __name__ == '__main__':
    main()
