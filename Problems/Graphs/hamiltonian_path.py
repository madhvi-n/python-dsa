"""
Given an undirected graph, print all Hamiltonian paths present in it.
The Hamiltonian path in an undirected or directed graph is a path that visits each vertex exactly once.
A complete graph has n! hamiltonian cycles.
"""


# Time complexity: O(n!)
# Space complexity: O(n)
def find_hamiltonian_paths(n: int, edges: list[list]):
    result = []

    def dfs(src, visited, path):
        if len(path) == n:
            result.append(path[:])

        for adjacent in range(n):
            if not visited[adjacent]:
                visited[adjacent] = True
                path.append(adjacent)

                dfs(adjacent, visited, path)

                visited[adjacent] = False
                path.pop()

    for i in range(n):
        path = [i]
        visited = [False] * n
        visited[i] = True
        dfs(i, visited, path)

    print(len(result))
    return result


def main():
    print(find_hamiltonian_paths(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]))
    print(find_hamiltonian_paths(7, [(0, 1), (1, 2), (0, 3), (2, 3), (0, 4), (2, 3)]))


if __name__ == '__main__':
    main()
