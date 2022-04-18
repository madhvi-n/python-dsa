"""
Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""


def binary_search(nums: list, target: int, find_start_index: bool) -> int:
    ans, start, end = -1, 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            ans = mid
            if find_start_index:
                end = mid - 1
            else:
                start = mid + 1
    return ans


def search_range(nums, target):
    ans = [-1, -1]
    ans[0] = binary_search(nums, target, True)
    if ans[0] != -1:
        ans[1] = binary_search(nums, target, False)
    return ans


def search_range_2(nums, target):
    def search(nums: list, target: int, first: bool) -> int:
        result = -1

        if not nums:
            return result

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result

    first = search(nums, target, first=True)

    if first != -1:
        last = search(nums, target, first=False)
    else:
        last = -1

    return [first, last]


def main():
    print(search_range([5, 7, 7, 8, 8, 10], 8))
    print(search_range_2([5, 7, 7, 8, 8, 10], 8))


if __name__ == '__main__':
    main()
