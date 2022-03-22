"""
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
"""
from typing import List

def max_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = float('-inf')
    cur_sum = 0
    start = 0
    for index, val in enumerate(nums):
        cur_sum += val
        if index - start + 1 == k:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= nums[start]
            start += 1
    return max_sum


def main():
    print(max_subarray_sum([10, 20, 30, 40, 50, 60], 4))
    print(max_subarray_sum([10, 20, 30, 40, 50, 60, 70], 2))


if __name__ == '__main__':
    main()
