"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

# Naive approach -> For loop and keep track of minimum
# Efficient approach -> Binary search


def find_minimum(nums: list) -> int:
    start = 0
    end = len(nums) - 1

    res = nums[0]

    while start <= end:
        if nums[start] < nums[end]:
            res = min(res, nums[start])
            break

        mid = start + (end - start) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[start]:
            start = mid + 1
        else:
            end = mid - 1
    return res


def find_maximum(nums: list) -> int:
    start = 0
    end = len(nums) - 1

    res = nums[0]

    while start <= end:
        if nums[start] < nums[end]:
            res = max(res, nums[start])
            break

        mid = start + (end - start) // 2
        res = max(res, nums[mid])

        if nums[mid] >= nums[start]:
            start = mid + 1
        else:
            end = mid - 1
    return res


def main():
    print(find_minimum([4, 5, 6, 7, 0, 1, 2]))
    print(find_maximum([4, 5, 6, 7, 0, 1, 2]))
    print(find_minimum([3, 4, 5, 1, 2]))
    print(find_maximum([3, 4, 5, 1, 2]))


if __name__ == '__main__':
    main()
