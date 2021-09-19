"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

def findMaxConsecutiveOnes(nums):
    # intitialize count
    count = 0

    # initialize max
    result = 0

    for i in range(0, len(nums)):
        # Reset count when 0 is found
        if (nums[i] == 0):
            count = 0
        else:
            # increase count when 1 is found
            count += 1
            result = max(result, count)
    return result


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 0, 0, 1, 1, 1]
    result = findMaxConsecutiveOnes(nums)
    print(f"Max consecutive 1's in the array: {result}")
