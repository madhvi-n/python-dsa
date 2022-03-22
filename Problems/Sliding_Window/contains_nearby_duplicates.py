
"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List

def contains_nearby_duplicates(nums: List[int], k: int) -> bool:
    window = set()
    i, j = 0, 0

    while i < len(nums) and j < len(nums):
        if j - i > k:
            window.remove(nums[i])
            i += 1

        if nums[j] in window:
            return True

        window.add(nums[j])
        j += 1

    return False


def main():
    print(contains_nearby_duplicates([1,2,3,1], 3))

if __name__ == '__main__':
    main()
