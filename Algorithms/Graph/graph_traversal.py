"""
Complexity Analysis:
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity: O(V), since an extra visited array of size V is required.

"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, source):
        visited = [False] * (max(self.graph) + 1)

        # Mark the source node as visited and enqueue it
        queue = [source]
        visited[source] = True
        while queue:
            # dequeue the first vertex and print it
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for node in self.graph[vertex]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

    def dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for node in self.graph[vertex]:
            if node not in visited:
                self.dfs_helper(node, visited)

    def dfs(self, vertex):
        visited = set()
        self.dfs_helper(vertex, visited)


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.bfs(2)
    print()
    g.dfs(2)


if __name__ == '__main__':
    main()
