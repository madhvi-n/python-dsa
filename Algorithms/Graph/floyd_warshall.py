"""
Time complexity: O(V ^ 3)
Space complexity: O(V ^ 2)
"""


def find_all_shortest_paths(n: int, graph: list[list]):
    distance = graph[:]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                # if distance[i][k] == float('inf') or distance[k][j] == float('inf'):
                #     continue
                # elif distance[i][k] + distance[k][j] < distance[i][j]:
                #     distance[i][j] = distance[i][k] + distance[k][j]

    # check for negative cycle
    for i in range(n):
        if distance[i][i] < 0:
            print("Negative edge weight cycle found in graph")

    for row in distance:
        print(row)


def main():
    graph = [
        [0, 1, 4, float('inf'), float('inf'), float('inf')],
        [float('inf'), 0, 2, 4, 7, float('inf')],
        [float('inf'), float('inf'), 0, 3, 4, float('inf')],
        [float('inf'), float('inf'), float('inf'), 0, float('inf'), 4],
        [float('inf'), float('inf'), float('inf'), 3, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), 5, 0],
    ]
    find_all_shortest_paths(6, graph)


if __name__ == '__main__':
    main()
