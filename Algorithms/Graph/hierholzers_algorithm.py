"""
Given a directed Eulerian graph, print an Euler circuit.
Euler circuit is a path that traverses every edge of a graph, and the path ends on the starting vertex.

Remember that a directed graph has a Eulerian cycle if the following conditions are true -
(1) All vertices with nonzero degrees belong to a single strongly connected component.
(2) In degree and out-degree of every vertex is the same.
The algorithm assumes that the given graph has a Eulerian Circuit

Algorithm:
Start from a vertex. Initialize current_path and circuit hashmap
Keep visiting its adjacent edges and maintain the visited in current_path
If there are no adjacent edges, we put the vertex in curcuit and backtrack till we find unvisited edges

Consider a directed graph with edges [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 1]]

adjacency_list =  {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [4],
    4: [1]
}
Start from vertex 0 : current_path = {0}, circuit = {}
Visiting edge 0 -> 1 : current_path = {0, 1} circuit = {}
Visiting edge 1 -> 2 : current_path = {0, 1, 2} circuit = {}
Visiting edge 2 -> 0 : From 2 we go back to 0 which is already visited and has no unvisited adjacent
edges, so we put 0 in circuit and backtrack till we find an edge

current_path = {0, 1, 2} circuit = {0}
From 0, we backtrack to 2. Since 2 has no unvisited adjacent edges, we add it to circuit and remove from current path
current_path = {0, 1} circuit = {0, 2}. Backtracking to 1 again.

Visiting edge 1 -> 3, current_path = {0, 1, 3} circuit = {0, 2}
Visiting edge 3 -> 4, current_path = {0, 1, 3, 4} circuit = {0, 2}
Visiting edge 4 -> 1, current_path = {0, 1, 3, 4, 1} circuit = {0, 2}

Since all edges have been used or visited, we pop edge from current_path one by one and add it to circuit
In the end the circuit = {0, 2, 1, 4, 3, 1, 0}
We print the circuit in reverse to obtain the path followed
"""
from collections import defaultdict


# Time complexity: O (V + E)
def euler_circuit(n: int, edges: list[list]):
    current_path = []
    circuit = []
    adjacency_list = defaultdict(list)

    for src, dest in edges:
        adjacency_list[src].append(dest)

    current_path.append(0)

    while current_path:
        curr_vertex = current_path[-1]

        # if there's an adjacent edge of the current vertex, pop it from adjacent list and add it to current_path
        # else pop the top element and add it to circut
        if adjacency_list[curr_vertex]:
            next_vertex = adjacency_list[curr_vertex].pop()
            current_path.append(next_vertex)
        else:
            circuit.append(current_path.pop())

    print(circuit[::-1])


def main():
    edges = [[0, 1], [1, 2], [2, 0]]
    euler_circuit(3, edges)

    edges = [[0, 1], [0, 6], [1, 2], [2, 0], [2, 3], [3, 4], [4, 2], [4, 5], [5, 0], [6, 4]]
    euler_circuit(7, edges)


if __name__ == '__main__':
    main()
