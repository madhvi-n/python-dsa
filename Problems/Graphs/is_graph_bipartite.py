from collections import defaultdict


"""
    1st approach: BFS + nodes coloring
    Time    O(V+E)
    Space   O(V+E)
"""


def is_bipartite_bfs(n, edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    visited = {}

    def bfs(graph, start, visited):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in visited:
                if visited[pop] != color:
                    return False
                continue
            visited[pop] = color
            vertices = graph[pop]
            for v in vertices:
                q.append((v, -color))
        return True

    # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
    for i in range(len(graph)):
        if i not in visited:
            if not bfs(graph, i, visited):
                return False
    return True


"""
    2nd approach: recursive DFS + nodes coloring
    Time    O(V+E)
    Space   O(V+E)
"""


def is_bipartite_dfs(n, edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * n
    color = [False] * n
    src = 0

    # mark the src as visited and set it's color to False(0)
    visited[src] = True

    def dfs(v, visited, color):
        # for every edge from v to u
        for u in graph[v]:
            # if it's not visited
            if not visited[u]:

                # mark the node as visited. current node has the color opposite to the parent
                visited[u] = True
                color[u] = not color[v]

                if not dfs(u, visited, color):
                    return False

            # if it's visited and has the same color as of parent, return false
            elif color[v] == color[u]:
                return False
        return True

    return dfs(src, visited, color)


def check_if_bipartite(graph):
    color = {}

    def dfs(pos):
        for i in graph[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
            else:
                color[i] = 1 - color[pos]
                if not dfs(i):
                    return False
        return True

    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(i):
                return False
    return True


def main():
    print(is_bipartite_dfs(9, [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8), (1, 3)]))
    print(is_bipartite_bfs(9, [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8), (1, 3)]))

    print(is_bipartite_dfs(9, [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]))
    print(is_bipartite_bfs(9, [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]))


if __name__ == '__main__':
    main()
