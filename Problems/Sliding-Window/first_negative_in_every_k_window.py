"""
Given an array arr[] of size n and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.
Print 0 if there are no negative number.
"""
from typing import List


def first_negative_in_arr(nums: List[int], k: int) -> List[int]:
    res = []
    negatives = []
    start = 0
    for index, val in enumerate(nums):
        if val < 0:
            negatives.append(val)

        if index - start + 1 == k:
            if len(negatives) > 0:
                res.append(negatives[0])
                negatives.pop(0)
            else:
                pass
            start += 1
    return res

def main():
    res = first_negative_in_arr([12, -1, -7, 8, -15, 30, 16, 28], 3)
    print(res)


if __name__ == '__main__':
    main()
