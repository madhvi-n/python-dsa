"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports
of one flight. Reconstruct the itinerary in order and return it.
All the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""
from collections import defaultdict


def find_itinerary(tickets: list[list[str]]):
    graph = defaultdict(list)
    route = []

    for x, y in tickets:
        graph[x].append(y)

    for key in graph:
        graph[key] = sorted(graph[key], reverse=True)

    def dfs(src):
        while graph[src]:
            candidate = graph[src].pop()
            dfs(candidate)
        route.append(src)

    dfs("JFK")
    print(route[::-1])


def main():
    find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])


if __name__ == '__main__':
    main()
