from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self, vertex, color):
        # WHITE -> unvisited, GRAY -> visited, BLACK -> visited and processed
        color[vertex] = "GRAY"

        for v in self.graph[vertex]:
            if color[v] == "GRAY":
                return True

            if color[v] == "WHITE" and self.dfs(v, color):
                return True
        color[vertex] = "BLACK"
        return False

    def is_cyclic(self):
        color = ["WHITE"] * self.vertices

        for i in range(self.vertices):
            if color == "WHITE":
                if self.dfs(i, color):
                    return True
        return False


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.is_cyclic())


if __name__ == '__main__':
    main()
