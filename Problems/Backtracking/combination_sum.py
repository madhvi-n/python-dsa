"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def backtrack(index, current_combination, total):
        # if total equals to target, we found one combination so append a copy to result and return
        if total == target:
            result.append(current_combination[:])
            return

        # if index is out of bounds or total is greater than target, return
        if index >= len(candidates) or total > target:
            return

        # include the number at index in combination and call dfs with total + candidates[index]
        current_combination.append(candidates[index])
        backtrack(index, current_combination, total + candidates[index])

        # exclude candidates[index] and call dfs over next index
        current_combination.pop()
        backtrack(index + 1, current_combination, total)

    backtrack(0, [], 0)
    return result


def main():
    answer = combination_sum([2, 3, 6, 7], 7)
    print(answer)


if __name__ == '__main__':
    main()