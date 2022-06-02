"""
Merge sort

Time complexity: O(n* log n)
Space complexity: O(n)
"""
from typing import List


def merge_sort(arr: List[int], left: int, right: int) -> List[int]:
    # If arr has one element, return array
    if right - left <= 1:
        return arr[left: right]

    # Else call merge_sort recursively
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
        if i == m:  # arr1 is empty
            result.append(arr2[j])
            j += 1
        elif j == n:  # arr2 is empty
            result.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:  # Top element of arr1 is smaller
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result


def main():
    arr = [2, 4, 6, 8, 9, 15, 4, 3, 5, 16, 8, 2, 4, 8, 12, 7]
    res = merge_sort(arr, 0, len(arr))
    print(res)


if __name__ == '__main__':
    main()
