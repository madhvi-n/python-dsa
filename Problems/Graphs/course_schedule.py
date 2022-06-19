"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course 'bi' first
if you want to take course 'ai'.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
"""
from collections import defaultdict


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    visited = [0] * num_courses

    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i, visited):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False

        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True

        # mark as being visited
        visited[i] = -1

        # visit all the neighbours
        for j in graph[i]:
            if not dfs(j, visited):
                return False

        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True

    for i in range(num_courses):
        if not dfs(i, visited):
            return False
    return True


def can_finish_2(num_courses: int, prerequisites: list[list]) -> bool:
    pre_map = {i: [] for i in range(num_courses)}

    for course, pre in prerequisites:
        pre_map[course].append(pre)

    visited = set()

    def dfs(course):
        if course in visited:
            return False

        if not pre_map[course]:
            return True

        visited.add(course)

        for pre in pre_map[course]:
            if not dfs(pre):
                return False
        visited.remove(course)
        pre_map[course] = []
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True


def main():
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
    print(can_finish_2(2, [[1, 0], [0, 1]]))


if __name__ == '__main__':
    main()
