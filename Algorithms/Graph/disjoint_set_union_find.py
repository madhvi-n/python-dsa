from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest) -> None:
        self.graph[src].append(dest)

    def find_parent(self, parent, i) -> int:
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])

    def union_find(self, parent, x, y) -> None:
        parent[x] = y

    def is_cyclic(self) -> bool:
        parent = [-1] * (self.vertices + 1)

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)

                if x == y:
                    return True
                self.union_find(parent, x, y)
        return False


def is_cyclic(n: int, edges: list[list]):
    adjacency_list = defaultdict(list)

    for x, y in edges:
        adjacency_list[x].append(y)

    dsuf = [-1] * (n + 1)

    def find(v):
        if dsuf[v] == -1:
            return v
        return find(dsuf[v])

    def union_operation(x, y):
        x_parent = find(x)
        y_parent = find(y)
        dsuf[x_parent] = y_parent

    for x, y in edges:
        from_parent = find(x)
        to_parent = find(y)

        if from_parent == to_parent:
            return True

        union_operation(from_parent, to_parent)
    return False


def main():
    print(is_cyclic(3, [[0, 1], [1, 2], [2, 0]]))
    print(is_cyclic(4, [[1, 2], [1, 3], [2, 4], [4, 3]]))

    g = Graph(4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    print(g.is_cyclic())


if __name__ == '__main__':
    main()
