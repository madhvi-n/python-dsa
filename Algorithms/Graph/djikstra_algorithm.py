"""
Dijkstra's Algorithm:
Doesn't work for negative edges
Single source shortest path algorithm

Algorithm:
1. Mark all nodes are unvisited initially
2. Mark all nodes with distance inf except source node
3. Repeat the steps for V - 1 times:
    i. Pick min value node which is unvisited
    ii. Mark this node as visited
    iii. Update the adjacent nodes. If cost[u] + weight[uv] < cost[v], then update weight else discard

Time complexity: O(V ^ 2) or O(ElogV) using adjacency_list + min-heap
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


def find_shortest_path(n: int, graph: list[list]):
    processed = [False] * n
    parent = [None] * n
    distance = [float('inf')] * n

    # start node has no parent and distance is 0
    distance[0] = 0
    parent[0] = -1

    for i in range(n):
        # select min cost node
        u = select_min_vertex(distance, processed)
        processed[u] = True

        # check if there's an edge from u to j, which is unprocessed
        for j in range(n):
            if 0 < graph[u][j] and not processed[j] and\
                    (distance[u] + graph[u][j] < distance[j]):
                distance[j] = distance[u] + graph[u][j]
                parent[j] = u

    for i in range(n):
        print(f"{i} -> {distance[i]}")


def main():
    edges = [[0, 1, 4], [0, 2, 6], [1, 2, 6], [1, 3, 3], [1, 4, 4], [2, 3, 1], [3, 4, 2], [3, 5, 3], [4, 5, 7]]
    n = 6
    graph = create_adjacency_matrix(n, edges)
    find_shortest_path(n, graph)


if __name__ == '__main__':
    main()
