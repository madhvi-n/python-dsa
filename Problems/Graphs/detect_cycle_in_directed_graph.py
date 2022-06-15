from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self, vertex, visited, recursive_stack):
        visited[vertex] = True
        recursive_stack[vertex] = True

        for neighbor in self.graph[vertex]:
            if recursive_stack[neighbor]:
                return True
            elif not visited[neighbor]:
                if self.dfs(neighbor, visited, recursive_stack):
                    return True

        recursive_stack[vertex] = False
        return False

    def is_cyclic(self):
        visited = [False] * (self.vertices + 1)
        recursive_stack = [False] * (self.vertices + 1)

        for i in range(self.vertices):
            if not visited[i]:
                if self.dfs(i, visited, recursive_stack):
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
