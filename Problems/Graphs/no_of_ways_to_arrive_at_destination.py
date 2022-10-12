"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bidirectional roads between some
intersections. The inputs are generated such that you can reach any intersection from any other intersection and
that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road
between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel
from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time.
Since the answer may be large, return it modulo 10^9 + 7.

Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
"""
from collections import defaultdict


"""
Time complexity: O(V * V)
Space complexity: O(V * V)
"""


def count_paths(n: int, roads: list[list[int]]):
    graph = defaultdict(list)
    visited = [False] * n
    path = []
    res = defaultdict(list)
    rec = []
    for src, dest, time in roads:
        graph[src].append((dest, time))
        graph[dest].append((src, time))

    def dfs(src, dest, time, path, rec):
        rec.append("X")
        visited[src] = True
        path.append(src)

        if src == dest:
            res[time].append(path[:])

        for u, ut in graph[src]:
            if not visited[u]:
                dfs(u, dest, time + ut, path, rec)

        path.pop()
        visited[src] = False

    dfs(0, n - 1, 0, path, rec)
    min_time = min(res.keys())
    print(len(res[min_time]))


def main():
    count_paths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]])
    count_paths(2, [[1, 0, 10]])


if __name__ == '__main__':
    main()
