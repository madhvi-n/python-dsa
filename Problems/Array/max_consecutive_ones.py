"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""


def max_consecutive_ones(nums):
    # initialize count
    count = 0

    # initialize max
    result = 0

    for i in range(len(nums)):
        # Reset count when 0 is found
        if nums[i] == 0:
            count = 0
        else:
            # increase count when 1 is found
            count += 1
            result = max(result, count)
    return result


def main():
    nums = [1, 1, 0, 1, 0, 0, 1, 1, 1]
    result = max_consecutive_ones(nums)
    print(f"Max consecutive 1's in the array: {result}")


if __name__ == '__main__':
    main()
