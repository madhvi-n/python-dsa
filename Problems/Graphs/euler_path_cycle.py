"""
Check whether the graph is euler, semi-eulerian or not a euler graph
"""
from collections import defaultdict


# Undirected graph
# Time complexity O (V + E)
def find_euler_path_cycle(n: int, edges: list[list[int]]):
    adjacency_list = defaultdict(list)

    for x, y in edges:
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    def dfs(src, visited):
        visited[src] = True

        for adjacent in adjacency_list[src]:
            if not visited[adjacent]:
                dfs(adjacent, visited)

    def is_connected_graph():
        visited = [False] * n
        node = -1

        # find a node to start DFS
        for i in range(n):
            if len(adjacency_list[i]) > 0:
                node = i
                break

        # if node equals to -1, not start node was found meaning no edges present in graph
        if node == -1:
            return True

        dfs(node, visited)

        # check if all non-zero vertices are visited
        for i in range(n):
            if not visited[i] and len(adjacency_list[i]) > 0:
                return False
        return True

    def find_euler_path():
        # if graph is not component, then graph is multi component edged graph
        if not is_connected_graph():
            return 0

        # count odd degree vertices using adjacency list length
        odd = 0
        for i in range(n):
            if len(adjacency_list[i]) % 2 != 0:
                odd += 1

        # count = 0 -> eulerian
        # count = 2 -> semi eulerian
        # count > 2 -> not eulerian
        # Note that odd count can never be 1 for undirected graph
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        elif odd > 2:
            return 0

    count = find_euler_path()
    if count == 0:
        print("Graph is not Eulerian")
    elif count == 1:
        print("Graph has a Euler path")
    else:
        print("Graph has a Euler cycle")


def find_euler_cycle(n: int, edges: list[list]):
    # create adjacency list for edges
    # init indegree array for n vertices -> for every v to u, increment indegree at u
    # find if graph is strongly connected using kosaraju algorithm
    # if graph is not scc and length of indegree and outdegree of each vertex aren't same, not an eulerian else it is.
    ...


def main():
    find_euler_path_cycle(5, [[0, 1], [0, 2], [2, 1], [0, 3], [3, 4]])
    find_euler_path_cycle(5, [[1, 0], [0, 2], [2, 1], [0, 3], [4, 0], [3, 4]])
    find_euler_path_cycle(5, [[0, 1], [0, 2], [2, 1], [0, 3], [3, 4], [1, 3]])
    find_euler_path_cycle(3, [[0, 1], [1, 2], [2, 0]])


if __name__ == '__main__':
    main()
