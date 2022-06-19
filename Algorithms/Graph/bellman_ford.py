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


def find_shortest_path(n: int, edges: list[list]):
    parent = [None] * n
    distance = [float('inf')] * n

    parent[0] = -1
    distance[0] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return

    print(f"Vertex   \t  Distance from source")
    for i in range(n):
        print(f"{i} \t\t -> \t\t {distance[i]}")


def main():
    find_shortest_path(5, [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]])


if __name__ == '__main__':
    main()
