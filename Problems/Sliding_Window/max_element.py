"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from typing import List


def max_element(arr: List[int]): int:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)


    for key, val in count.items():
        if val > len(nums) // 2:
            return key

def main():
    max_element([2,3,2])
    max_element([2,2,1,1,1,2,2])

if __name__ == '__main__':
    main()
