from collections import defaultdict


class Node:
    def __init__(self, parent=-1, rank=0):
        self.parent = parent
        self.rank = rank


def union(subsets, u, v):
    # Attach smaller rank tree under root of high rank tree (union by rank)
    # If ranks are same, then make one as root and increment its rank by one
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


def is_cyclic(n: int, edges: list[list[int]]):
    graph = defaultdict(list)
    subsets = []

    for x, y in edges:
        graph[x].append(y)

    for i in range(n):
        subsets.append(Node(i, 0))

    for u in graph:
        u_rep = find(subsets, u)
        for v in graph[u]:
            v_rep = find(subsets, v)

            if u_rep == v_rep:
                return True
            else:
                union(subsets, u_rep, v_rep)


def main():
    a = is_cyclic(5, [[0, 1], [2, 3], [1, 2], [0, 4], [4, 3]])
    print(a)


if __name__ == '__main__':
    main()
