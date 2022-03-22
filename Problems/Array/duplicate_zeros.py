"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
"""
from typing import List


def duplicate_zeroes(arr: List[int]) -> List[int]:
    zeros = 0
    arr_length = len(arr) - 1

    for left in range(arr_length + 1):
        if left > arr_length - zeros:
            break

        if arr[left] == 0:
            if left == arr_length - zeros:
                arr[arr_length] = 0
                arr_length -= 1
                break
            zeros += 1

    last = arr_length - zeros

    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + zeros] = 0
            zeros -= 1
            arr[i + zeros] = 0
        else:
            arr[i + zeros] = arr[i]

    return arr


def main():
    arr = [1, 0, 2, 3, 0, 4, 5, 0, 0, 4]
    print(f"Original Array: {arr}")
    result = duplicate_zeroes(arr)
    print(f"Duplicate zeros: {result}")


if __name__ == '__main__':
    main()
