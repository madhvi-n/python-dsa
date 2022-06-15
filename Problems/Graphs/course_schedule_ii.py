"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if
you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of
them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""
from collections import defaultdict, deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    adjacency_list = defaultdict(list)

    # A pair [a, b] in the input represents edge from b --> a
    for dest, src in prerequisites:
        adjacency_list[src].append(dest)

    topological_order = []
    is_possible = True

    # By default, all vertces are WHITE
    color = {k: 1 for k in range(num_courses)}

    def dfs(node):
        nonlocal is_possible

        # Don't recurse further if we found a cycle already
        if not is_possible:
            return

        # Start the recursion
        color[node] = 2

        # Traverse on neighboring vertices
        if node in adjacency_list:
            for neighbor in adjacency_list[node]:
                if color[neighbor] == 1:
                    dfs(neighbor)
                elif color[neighbor] == 2:
                    # An edge to a GRAY vertex represents a cycle
                    is_possible = False

        # Recursion ends. We mark it as black
        color[node] = 3
        topological_order.append(node)

    for vertex in range(num_courses):
        # If the node is unprocessed, then call dfs on it.
        if color[vertex] == 1:
            dfs(vertex)

    return topological_order[::-1] if is_possible else []


def can_finish_using_kahns_algorithm(num_courses: int, prerequisites: list[list[int]]):
    adjacency_list = defaultdict(list)
    indegree = dict()
    topological_order = []

    for dest, src in prerequisites:
        adjacency_list[src].append(dest)
        indegree[dest] = 1 + indegree.get(dest, 0)

    queue = deque([k for k in range(num_courses) if k not in indegree])

    while queue:
        vertex = queue.popleft()
        topological_order.append(vertex)

        if vertex in adjacency_list:
            for node in adjacency_list[vertex]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
    return topological_order if len(topological_order) == num_courses else []


def main():
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
    print(can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    print()

    print(can_finish_using_kahns_algorithm(2, [[1, 0]]))
    print(can_finish_using_kahns_algorithm(2, [[1, 0], [0, 1]]))
    print(can_finish_using_kahns_algorithm(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


if __name__ == '__main__':
    main()
