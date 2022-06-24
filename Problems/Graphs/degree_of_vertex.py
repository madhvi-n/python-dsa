"""
Degree of vertex is no of outgoing edges from a particular node
"""


def degree_of_vertex(n: int, source, edges: list[list]):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for x, y in edges:
        matrix[x][y] = matrix[y][x] = 1

    degree = 0

    for i in range(n):
        if matrix[source][i] == 1:
            degree += 1
    if matrix[source][source] == 1:
        degree += 1
    print(f"Degree of vertex {source} : {degree}")


def main():
    n = 4
    edges = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]

    for i in range(n):
        degree_of_vertex(n, i, edges)


if __name__ == '__main__':
    main()
