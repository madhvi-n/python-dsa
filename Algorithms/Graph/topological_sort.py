"""
Topological sort -> Modified DFS

Algorithm:
1. Initialize a visited array of length vertices and an empty stack
2. Iterate through vertices and call dfs on vertex which are not visited
3. DFS -
    a. Mark the node as visited
    b. Call dfs recursively on the adjacent nodes of the current vertex which are not visited
    c. Append the current vertex to the stack
4. Return reversed(stack) or stack[::-1]

Time complexity: O(V + E)
Space complexity: O(V)
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True

        for v in self.graph[vertex]:
            if not visited[v]:
                self.dfs(v, visited, stack)
        stack.append(vertex)

    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        print(stack[::-1])


def main():
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.topological_sort()


if __name__ == '__main__':
    main()
