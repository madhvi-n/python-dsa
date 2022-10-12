"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def backtrack(index, current_combination, current_sum):
        # if current_sum == 0, then we have found one combination
        # if current_sum < 0, return
        if current_sum == 0:
            result.append(current_combination[:])
            return

        if current_sum < 0:
            return

        prev = -1

        for i in range(index, len(candidates)):
            if candidates[i] == prev:
                continue

            # include the current candidate in the combination and call dfs over next index,
            # with current_sum - current candidate

            current_combination.append(candidates[i])
            backtrack(i + 1, current_combination, current_sum - candidates[i])

            # exclude the current candidate and store current candidate in prev
            current_combination.pop()
            prev = candidates[i]

        backtrack(0, [], target)
        return result


def main():
    answer = combination_sum([10, 1, 2, 7, 6, 1, 5], 8)
    print(answer)


if __name__ == '__main__':
    main()
