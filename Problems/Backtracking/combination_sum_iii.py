"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""


def combination_sum(candidates: list[int], k: int, n: int) -> list[list[int]]:
    result = []
    combination = []

    def backtrack(length, current_combination, current_sum):
        if current_sum < 0 or length < 0:
            return

        if current_sum == 0 and length == 0:
            result.append(current_combination[:])
            return

        # if combination is not empty, start = combination[-1] else 1
        start = current_combination[-1] + 1 if current_combination else 1

        # iterate through i from start till 10, call dfs considering each index
        for i in range(start, 10):
            backtrack(length - 1, current_combination + [i], current_sum - i)

    backtrack(k, combination, n)
    return result
