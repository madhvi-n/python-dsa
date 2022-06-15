from collections import defaultdict


def valid_path(vertices: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    visited = set()

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    def dfs(src, dest, visited):
        if src == dest:
            return True

        if src in visited:
            return False

        visited.add(src)

        for node in graph[src]:
            if dfs(node, dest, visited):
                return True
        return False

    return dfs(source, destination, visited)


def main():
    print(valid_path(10, [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]], 5, 9))
    print(valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))


if __name__ == '__main__':
    main()
