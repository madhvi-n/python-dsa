"""
The transitive closure for a digraph G is a digraph G’ with an edge (i, j) corresponding to each directed path from
i to j in G. The resultant digraph G’ representation in the form of the adjacency matrix is called the connectivity
matrix.

For example, consider the following directed graph:
graph = [[0, 2], [1 ,0], [3, 1]]

Transitive Closure
Its connectivity matrix C is

1   0   1   0
1   1   1   0
0   0   1   0
1   1   1   1

The value of C[i][j] is 1 only if a directed path exists from vertex i to vertex j.
Note that all diagonal elements in the connectivity matrix are 1 since a path exists from every vertex to itself.
"""
from collections import defaultdict


"""
Time complexity -> O(V ^ 3)
Space complexity -> O(V ^ 2)
"""


def transitive_closure_using_floyd_warshall(n: int, edges: list[list]):
    graph = [[0 for _ in range(n)] for _ in range(n)]

    # all diagonal elements are 1 since every vertex has path to itself
    for i in range(n):
        graph[i][i] = 1

    # marking edges on graph
    for x, y in edges:
        graph[x][y] = 1

    # shallow copy graph as matrix since initially both are same
    matrix = graph[:]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = matrix[i][k] and matrix[k][j]
    print(matrix)


"""
Time complexity -> O(V ^ 2) for sparse graph and O(V ^ 3) for dense graph since E = V ^ 2 in dense graph
Space complexity -> O(V ^ 2)
"""

    
def transitive_closure(n: int, edges: list[list]):
    adjacency_list = defaultdict(list)

    for src, dest in edges:
        adjacency_list[src].append(dest)

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    def dfs(root, v):
        for u in adjacency_list[v]:
            if matrix[root][u] == 0:
                matrix[root][u] = 1
                dfs(root, u)

    for i in range(n):
        matrix[i][i] = 1
        dfs(i, i)

    print(matrix)


def main():
    edges = [[0, 2], [1, 0], [3, 1]]
    transitive_closure(4, edges)
    transitive_closure_using_floyd_warshall(4, edges)


if __name__ == '__main__':
    main()
