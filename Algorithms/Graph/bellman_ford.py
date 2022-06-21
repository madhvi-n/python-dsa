"""
Bellman ford algorithm

Algorithm:
1. Initialize distance array with inf for all values except source(0)
2. Relax all the adjacent nodes for V - 1 times:
    - If d[u] + cost[uv] < d[v], then update d[v] with the min value else discard it
3. Relax all vertices once again and check if we find any new shortest path. If yes, there exists a negative edge
cycle in graph

Time complexity: O(V * E)
"""


def get_path(parent, vertex):
    if vertex and vertex < 0:
        return []
    return get_path(parent, parent[vertex]) + [vertex]


def find_shortest_path(n: int, source: int, edges: list[list]):
    parent = [-1] * n
    distance = [float('inf')] * n

    distance[source] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            # if distance to destination can be shortened by taking the edge (u, v)
            # update distance to new lower value and set parent of v as u
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u

    # run relaxation step once more to check for negative edge weight cycle
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return

    for i in range(n):
        if i != source and distance[i] < float('inf'):
            print(f'The distance of vertex {i} from vertex {source} is {distance[i]}. '
                  f'Its path is', get_path(parent, i))


def main():
    edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]
    n = 5
    for source in range(n):
        find_shortest_path(n, source, edges)


if __name__ == '__main__':
    main()
