"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

def sortedSquares(nums):
    result = [abs(nums[i]) ** 2 for i in range(0, len(nums))]
    return sorted(result)


def main():
    nums = [-4, -5, 2, 8, -3]
    result = sortedSquares(nums)
    print(f"Sorted array: {result}")


if __name__ == '__main__':
    main()
