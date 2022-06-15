"""
There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from
city from 'i' to city 'toi' with cost 'pricei'.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""
from collections import deque, defaultdict


# Using BFS -> Time and Space : O (V + E)
def cheapest_flight(n: int, flights: list[list[int]], src: int, dst: int, k: int):
    graph = defaultdict(list)
    deque_vert = deque([[src, 0, 0]])
    min_price = float('inf')

    for i, j, w in flights:
        graph[i].append([j, w])

    while deque_vert:
        city, visited, price = deque_vert.popleft()

        if price <= min_price and visited <= k and city != dst:
            for vertex, fare in graph[city]:
                deque_vert.append([vertex, visited + 1, price + fare])

        if city == dst:
            min_price = min(min_price, price)

    return min_price if min_price != float('inf') else -1


def main():
    print(cheapest_flight(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
    print(cheapest_flight(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))


if __name__ == '__main__':
    main()
