"""
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between
nodes 'ai' and 'bi' in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""


def find_redundant_connection(edges: list[list[int]]):
    length = len(edges)
    parent = [i for i in range(length + 1)]
    rank = [1 for _ in range(length + 1)]

    def find(p):
        p = parent[p]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True

    for x, y in edges:
        if not union(x, y):
            return [x, y]


def main():
    print(find_redundant_connection([[1, 2], [1, 3], [2, 3]]))
    print(find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))


if __name__ == '__main__':
    main()
