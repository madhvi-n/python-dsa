"""
https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater element that is to the right of x
in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element
of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array answer of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""


# Time: O(n^2)
def next_greater_element(nums1: list, nums2: list) -> list:
    res = []
    for j in range(len(nums1)):
        j_max = nums1[j]
        for i in range(nums2.index(j_max), len(nums2)):
            if nums2[i] > nums1[j]:
                j_max = nums2[i]
                break
            else:
                continue
        if j_max == nums1[j]:
            res.append(-1)
        else:
            res.append(j_max)

    return res


# Time: O(n * m)
def next_greater_element_2(nums1: list, nums2: list) -> list:
    nums1_index = {num: index for index, num in enumerate(nums1)}
    res = [-1] * len(nums1)

    for i in range(len(nums2)):
        if nums2[i] not in nums1_index:
            continue

        for j in range(i + 1, len(nums1)):
            if nums2[j] > nums1[i]:
                idx = nums1_index[nums2[i]]
                res[idx] = nums2[j]
                break
    return res


# Time: O(m + n)
def next_greater_num(nums1: list, nums2: list) -> list:
    nums1_index = {num: index for index, num in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = nums1_index[val]
            res[idx] = cur
        if cur in nums1_index:
            stack.append(cur)
    return res


def main():
    pass


if __name__ == '__main__':
    main()
