"""
Linear search

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

def linear_search(nums: List[int], target: int) -> int:
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1


def main():
    nums = [1,3,5,6,7,8,9,11,13,45,56,78]
    print(linear_search(nums, 58))
    print(linear_search(nums, 45))
    print(linear_search(nums, 11))

if __name__ == '__main__':
    main()
