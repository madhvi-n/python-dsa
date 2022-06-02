"""
Binary search

Time complexity: O(log n)
Space complexity: O(n)
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums)

    while start < end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def main():
    nums = [1, 3, 5, 6, 7, 8, 9, 11, 13, 45, 56, 78]
    print(binary_search(nums, 58))
    print(binary_search(nums, 45))
    print(binary_search(nums, 11))


if __name__ == '__main__':
    main()
