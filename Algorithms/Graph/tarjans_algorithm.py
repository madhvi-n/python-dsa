"""
Tarjan's algorithm for strongly connected components

Time complexity: O(V+E)
Space complexity: O(V)

"""
from collections import defaultdict


def find_scc(n: int, edges):
    adjacency_list = defaultdict(list)

    for src, dest in edges:
        adjacency_list[src].append(dest)

    disc = [-1] * n
    stack_member = [False] * n
    low = [-1] * n
    stack = []
    time = 0

    def dfs(v, disc, low, stack, stack_member, time):
        disc[v] = low[v] = time
        time += 1
        stack.append(v)
        stack_member[v] = True

        for u in adjacency_list[v]:
            if disc[u] == -1:
                dfs(u, disc, low, stack, stack_member, time)
                low[v] = min(low[v], low[u])
            elif stack_member[u]:
                low[v] = min(low[v], disc[u])

        top = -1
        if low[v] == disc[v]:
            while top != v:
                top = stack.pop()
                print(top, end=" ")
                stack_member[top] = False
            print()

    for i in range(n):
        if disc[i] == -1:
            dfs(i, disc, low, stack, stack_member, time)


def main():
    find_scc(7, [[0, 1], [1, 2], [1, 3], [3, 4], [4, 0], [4, 5], [4, 6], [5, 6], [6, 5]])
    print()

    edges = [
        [0, 1], [0, 3], [1, 2], [1, 4], [2, 0], [2, 6], [3, 2], [4, 5],
        [4, 6], [5, 6], [5, 7], [5, 8], [5, 9], [6, 4], [7, 9], [8, 9], [9, 8]
    ]
    find_scc(11, edges)


if __name__ == '__main__':
    main()
