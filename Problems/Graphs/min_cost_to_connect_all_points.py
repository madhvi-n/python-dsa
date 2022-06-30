"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path
between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
"""
import heapq


# Prim's algorithm
def min_cost_connect_points(points: list[list]):
    n = len(points)

    adjacency_list = {i: [] for i in range(n)}
    for i in range(n):
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adjacency_list[i].append([dist, j])
            adjacency_list[j].append([dist, i])

    result = 0
    visited = set()
    min_heap = [[0, 0]]  # [cost, point]
    while len(visited) < n:
        cost, i = heapq.heappop(min_heap)
        if i in visited:
            continue
        result += cost
        visited.add(i)

        for adjacent_cost, adjacent in adjacency_list[i]:
            if adjacent not in visited:
                heapq.heappush(min_heap, [adjacent_cost, adjacent])
    return result


def main():
    print(min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]))


if __name__ == '__main__':
    main()
