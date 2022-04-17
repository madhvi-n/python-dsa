"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
"""
# Time complexity: O(n)
# Space complexity: O(1)


def left_rotation(nums, k):
    if k == 0:
        return nums

    n = len(nums)
    k = k % n
    
    # Reverse arr[:k], then reverse arr[k:] and lastly reverse whole array
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, n - 1)
    reverse_array(nums, 0, n - 1)
    return nums


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
            

def main():
    nums = [x for x in range(1, 11)]
    print(left_rotation(nums, 3))

    nums = [x for x in range(1, 11)]
    print(right_rotation(nums, 3))


if __name__ == '__main__':
    main()
