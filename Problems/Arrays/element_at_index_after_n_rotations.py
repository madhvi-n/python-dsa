"""
Find element at given index after right circular rotations on elements at indices in the ranges[start, end]
"""


def right_rotation(nums, k):
    if k == 0:
        return nums

    n = len(nums)

    k = k % n

    # Reverse full array, then reverse arr[:k] and lastly reverse arr[k:]
    reverse_array(nums, 0, n - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, n - 1)
    return nums


def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1


def helper(nums, start, end):
    import collections
    nums = collections.deque(nums)
    nums.rotate(1)


def find_element(arr, ranges, index) -> int:
    for i in range(len(ranges)):
        [start, end] = ranges[i]
        helper(arr, start, end)
        print(arr)
    return arr[index]


def main():
    arr = [1, 2, 3, 4, 5]
    print(find_element(arr, [[0, 2], [0, 3]], 1))


if __name__ == '__main__':
    main()
