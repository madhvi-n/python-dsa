"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

from typing import List

def min_subarray_sum(nums: List[int], target: int) -> int:
    left = 0 # keep track of left pointer
    rsum = 0 # keep the running sum
    res = None # Answer we will return

    # Iterate through the array, the index will be your right pointer
    for right in range(len(nums)):

        # Add the current value to the running sum
        rsum += nums[right]

        # Once you reach the a value at or equal to the target you
        # can use a while loop to start subtracting the values from left
        # to right so that you can produce the minimum size subarray
        while rsum >= target:

            # The result is either the current result you have,
            # or the count of numbers from the current left position
            # to the rightmost position. You need it to be right + 1
            # because index starts at 0 (if you based the right as the
            # last index it would be 4 or len(nums) - 1)

            # If res is None we compare it against the max float,
            # saves us from having an if/else
            res = min(res or float('inf'), right + 1 - left)

            # Subtract the number to see if we can continue subtracting based
            # on the while loop case and increment the left pointer
            rsum -= nums[left]
            left += 1

    return res or 0

def main():
    a1 = min_subarray_sum([1,1,1,1,1,1,1,1], 11)
    print(a1)

    a2 = min_subarray_sum([2,3,1,2,4,3], 7)
    print(a2)

    a3 = min_subarray_sum([1,4,4], 4)
    print(a3)

if __name__ == '__main__':
    main()
