"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


def remove_duplicates(nums):
    return list(set(nums))


def remove_duplicates2(nums):
    last = nums[0]
    for index, num in enumerate(nums):
        print(index, last, num)
        if last == num:
            nums.pop(index)
        last = num
    return nums


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_duplicates(nums)
    # print(f"Array: {result}")

    arr = remove_duplicates2(nums)
    print(arr)


if __name__ == '__main__':
    main()
