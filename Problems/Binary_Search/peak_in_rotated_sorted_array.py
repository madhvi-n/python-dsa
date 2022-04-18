"""
Find the peak element in rotated sorted array
"""

# Naive approach -> For loop and keep track of minimum
# Efficient approach -> Binary search


def find_peak(nums: list) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2

        if nums[mid] > nums[mid + 1]:
            # Currently, in desc part of the array, search left
            end = mid
        else:
            start = mid + 1

    return start


def main():
    print(find_peak([4, 5, 6, 7, 0, 1, 2]))
    print(find_peak([3, 4, 5, 1, 2]))
    print(find_peak([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
