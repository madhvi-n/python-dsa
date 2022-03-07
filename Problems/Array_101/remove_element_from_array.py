"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def remove_element(nums, val):
    n = len(nums)
    nums = [nums.remove(val) for i in range(nums.count(val))]
    return n - len(nums)


def main():
    nums = [1, 2, 3, 3, 8, 4, 3]
    val = 3
    result = remove_element(nums, val)
    print(f"Remaining elements: {result}")


if __name__ == '__main__':
    main()
