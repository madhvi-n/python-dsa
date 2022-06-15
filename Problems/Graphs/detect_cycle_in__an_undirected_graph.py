"""
Time Complexity: O(V+E).
The program does a simple DFS Traversal of the graph which is represented using adjacency list.
So the time complexity is O(V+E).
Space Complexity: O(V).
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def dfs(self, vertex, visited, parent):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if not visited[i]:
                if self.dfs(i, visited, vertex):
                    return True
            elif parent != i:
                return True
        return False

    def is_cyclic(self):
        visited = [False] * self.vertices
        for i in range(self.vertices):
            if not visited[i]:
                if self.dfs(i, visited, -1):
                    return True
        return False


def main():
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print(g.is_cyclic())


if __name__ == '__main__':
    main()
