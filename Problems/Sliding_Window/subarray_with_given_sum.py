"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
N = 5, S = 12
arr = [1,2,3,7,5]
Output: [2, 4]
Explanation: The sum of elements from 2nd position to 4th position is 12.

Input:
N = 10, S = 15
arr = [1,2,3,4,5,6,7,8,9,10]
Output: [1, 5]
Explanation: The sum of elements from 1st position to 5th position is 15.
"""

from typing import List

def subarray_given_sum(arr: List[int], n:int, s:int) -> List[int]:
    pass


def main():
    print(subarray_given_sum([1,2,3,7,5], 5, 12))
    print(subarray_given_sum([1,2,3,4,5,6,7,8,9,10], 10, 15))


if __name__ == '__main__':
    main()
