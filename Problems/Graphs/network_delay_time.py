"""
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output:
"""
import heapq
from collections import defaultdict, deque


def network_delay_time(n: int, edges: list[list[int]], k: int):
    graph = defaultdict(list)
    t = [0] + [float('inf')] * n
    queue = deque([(0, k)])

    for u, v, w in edges:
        graph[u].append((v, w))

    while queue:
        time, node = queue.popleft()

        if time < t[node]:
            t[node] = time

        for adjacent, ut in graph[node]:
            queue.append((time + ut, adjacent))

    max_time = max(t)
    res = max_time if max_time < float('inf') else -1
    print(res)


def delayed_time(n: int, times: list[list], k: int):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    distance = {node: float("inf") for node in range(1, n + 1)}

    def dfs(distance, node, time_so_far):
        if time_so_far >= distance[node]:
            # signal has already reached this node. so no need to explore further
            return
        distance[node] = time_so_far
        for neighbour, time in sorted(graph[node]):
            dfs(distance, neighbour, time_so_far + time)

    dfs(distance, k, 0)
    total_time = max(distance.values())
    res = total_time if total_time < float("inf") else -1
    print(res)


def network_delay_time_ii(n: int, times: list[list], k: int):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    min_heap = [(0, k)]
    visited = set()
    t = 0

    while min_heap:
        w1, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        t = max(t, w1)

        for adjacent, time in graph[node]:
            if adjacent not in visited:
                heapq.heappush(min_heap, (w1 + time, adjacent))
    return t if len(visited) == n else -1


def main():
    network_delay_time(4, [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 2)
    print(network_delay_time_ii(4, [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 2))
    delayed_time(2, [[1, 2, 1], [2, 1, 3]], 2)


if __name__ == '__main__':
    main()
