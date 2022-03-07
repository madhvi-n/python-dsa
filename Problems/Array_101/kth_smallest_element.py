"""
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
"""
from typing import List

def merge_sort(arr: List[int], left: int, right: int) -> List[int]:
    if right - left <= 1:
        return arr[left: right]

    if right - left > 1:
        mid = (left + right) // 2
        first = merge_sort(arr, left, mid)
        second = merge_sort(arr, mid, right)
        return merge(first, second)

def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    result = []
    m, n = len(arr1), len(arr2)
    i, j = 0, 0

    while i + j < m + n:
        if i == m:
            result.append(arr2[j])
            j += 1
        elif j == n:
            result.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result

def kth_smallest(nums: List[int], k: int) -> int:
    sorted_array = merge_sort(nums, 0, len(nums))
    return sorted_array[k - 1]

def main():
    print(kth_smallest([7,10,4,3,20,15], 3))

if __name__ == '__main__':
    main()
