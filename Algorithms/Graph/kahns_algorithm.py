"""
Uses BFS to find topological sort

Algorithm:
1. Initialize an indegree array (of length vertices) or dict (with keys as vertices)
    a. Indegree for edges can be calculated by iterating over edge which is in the form of [src, dest]
    b. indegree[dest] += 1
    c. If a graph is given, indegree can be calculated using two loops.
2. Create adjacency_list for the edges.
3. Initialize an empty stack for topological order and queue for bfs, init count as 0
4. BFS -
    a. Pop the first element from queue (from the left), push it to stack
    b. Decrement the indegree for the adjacent nodes of the popped vertex. If indegree is 0, push it to queue.
    c. Increment count by 1
5. If count is not equal to vertices, cycle exists in graph and hence graph is not a DAG.

Time complexity: O(V + E)
Space complexity: O(V)
"""
from collections import defaultdict, deque


def topological_sort(n: int, edges: list[list[int]]):
    adjacency_list = defaultdict(list)
    indegree = dict.fromkeys(range(n), 0)
    count = 0
    queue = deque()
    stack = []

    for src, dest in edges:
        indegree[dest] += 1
        adjacency_list[src].append(dest)

    for key, val in indegree.items():
        if val == 0:
            queue.append(key)

    while queue:
        vertex = queue.popleft()
        stack.append(vertex)

        for node in adjacency_list[vertex]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
        count += 1

    if count == n:
        print(f"Topological sort order {stack}")
    else:
        print("Cycle found in graph. Not a DAG.")


def main():
    topological_sort(6, [[5, 3], [5, 0], [4, 0], [4, 1], [2, 1], [3, 0], [3, 2]])
    topological_sort(4, [[0, 1], [1, 2], [2, 3], [3, 1]])


if __name__ == '__main__':
    main()
