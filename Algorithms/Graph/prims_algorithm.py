"""
Prim's algorithm for minimum spanning tree

Time complexity: O(V ^ 2)
Space complexity: O(V)
"""


def create_adjacency_matrix(n, edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for x, y, w in edges:
        matrix[x][y] = w
        matrix[y][x] = w
    return matrix


def select_min_vertex(distance, visited):
    minimum = float('inf')
    vertex = None

    for i in range(len(visited)):
        if not visited[i] and distance[i] < minimum:
            vertex = i
            minimum = distance[i]
    return vertex


def find_mst(n: int, graph: list[list]):
    visited = [False] * n
    parent = [None] * n
    distance = [float('inf')] * n

    # start node has no parent and distance is 0
    distance[0] = 0
    parent[0] = -1

    for i in range(n):
        # select the vertex with min weight by applying greedy method
        u = select_min_vertex(distance, visited)
        visited[u] = True

        # relax adjacent vertices which are not visited
        for j in range(n):
            # 3 constraints to be considered while relaxing an edge
            # it must be present from u to j, vertex j is not visited, edge weight is smaller than the current
            #  edge weight from u to j must be between 0 to distance[j]
            if 0 < graph[u][j] < distance[j] and not visited[j]:
                distance[j] = graph[u][j]
                parent[j] = u

    for i in range(1, n):
        print(f"Edge {parent[i]} -> {i}, Weight: {graph[i][parent[i]]}")


def main():
    edges = [[0, 1, 4], [0, 2, 6], [1, 2, 6], [1, 3, 3], [1, 4, 4], [2, 3, 1], [3, 4, 2], [3, 5, 3], [4, 5, 7]]
    n = 6
    graph = create_adjacency_matrix(n, edges)
    find_mst(n, graph)
    print()
    graph = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]
    find_mst(5, graph)


if __name__ == '__main__':
    main()
