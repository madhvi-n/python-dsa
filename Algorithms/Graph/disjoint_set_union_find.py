from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

        for src, dest in edges:
            self.adjacency_list[src].append(dest)


class DisjointSet:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, k) -> int:
        # if k is root
        if self.parent[k] == k:
            return k

        # recurse till we find the root
        return self.find(self.parent[k])

    def union(self, x, y) -> None:
        # find the root of the sets in which elements `x` and `y` belongs
        a = self.find(x)
        b = self.find(y)
        self.parent[a] = b


def find_cycle(n: int, edges: list[list]):
    g = Graph(n, edges)

    ds = DisjointSet(n)

    for u in range(n):
        for v in g.adjacency_list[u]:
            from_parent = ds.find(u)
            to_parent = ds.find(v)

            if from_parent == to_parent:
                return True
            else:
                ds.union(from_parent, to_parent)
    return False


def main():
    print(find_cycle(3, [[0, 1], [1, 2], [2, 0]]))
    print(find_cycle(12, [[0, 1], [0, 6], [0, 7], [1, 2], [1, 5], [2, 3],
        [2, 4], [7, 8], [7, 11], [8, 9], [8, 10], [10, 11]]))


if __name__ == '__main__':
    main()
