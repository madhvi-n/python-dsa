"""
Time Complexity: O(V+E).
The program does a simple DFS Traversal of the graph which is represented using adjacency list.
So the time complexity is O(V+E).
Space Complexity: O(V).
"""
from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)

    def dfs(self, vertex, visited, parent=-1):
        # mark current vertex as visited and visit it's adjacent nodes
        visited[vertex] = True
        for u in self.adjacency_list[vertex]:
            # for each unvisited adjacent node, call dfs recursively
            if not visited[u]:
                if self.dfs(u, visited, vertex):
                    return True

            # if adjancent node is visited and adjacent node is not a parent, we found a cross edge
            elif u != parent:
                return True
        return False

    def bfs(self, src):
        queue = deque()
        visited = [False] * self.vertices
        visited[src] = True
        queue.append((src, -1))

        while queue:
            v, parent = queue.popleft()
            for u in self.adjacency_list[v]:
                if not visited[u]:
                    visited[u] = True
                    queue.append((u, v))
                elif u != parent:
                    return True
        return False

    def has_cycle_bfs(self):
        return self.bfs(0)

    def has_cycle(self):
        visited = [False] * self.vertices
        if self.dfs(0, visited):
            return True
        return False


def main():
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print(g.has_cycle())
    print(g.has_cycle_bfs())

    g = Graph(12)
    g.add_edge(0, 1)
    g.add_edge(0, 6)
    g.add_edge(0, 7)
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(7, 8)
    g.add_edge(7, 11)
    g.add_edge(8, 9)
    g.add_edge(8, 10)
    print(g.has_cycle())
    print(g.has_cycle_bfs())

    g.add_edge(5, 9)
    print(g.has_cycle())
    print(g.has_cycle_bfs())


if __name__ == '__main__':
    main()
