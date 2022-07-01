"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
that there is an edge between ai and bi in the graph.
Return the number of connected components in the undirected graph.

Example:
    Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
    Output: 2
"""


# Union find
def connected_components(n: int, edges: list[list[int]]):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(p):
        p = parent[p]
        while p != parent[p]:
            # path compression
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(x, y):
        p1, p2 = find(x), find(y)

        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for x, y in edges:
        if union(x, y) == 1:
            res -= 1
    return res


def main():
    print(connected_components(5, [[0, 1], [1, 2], [3, 4]]))


if __name__ == '__main__':
    main()
