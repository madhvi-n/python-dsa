"""
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
"""
from typing import List

def count_distinct(nums: List[int], n: int, k: int) -> List[int]:
    result = []
    count = dict()

    for i in range(k):
        count[nums[i]] = 1 + count.get(nums[i], 0)
    result.append(len(count))

    left = 0
    for j in range(k, n):
        count[nums[j]] = 1 + count.get(nums[j], 0)

        count[nums[left]] -= 1

        if count[nums[left]] == 0:
            count.pop(nums[left])

        result.append(len(count))

        left += 1

    return result

def main():
    print(count_distinct([1,2,1,3,4,2,3], 7, 4))
    print(count_distinct([1,2,1,3,4,2,3], 7, 3))
    print(count_distinct([4,1,1], 3, 2))

if __name__ == '__main__':
    main()
