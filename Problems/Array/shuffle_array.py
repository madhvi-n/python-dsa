"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List


def shuffle_array(nums: List[int], n: int) -> List[int]:
    arr1 = nums[:n]
    arr2 = nums[n:]

    result = [];

    for i in range(0, n):
        result.append(arr1[i]);
        result.append(arr2[i]);
    return result


def main():
    nums = [2,5,1,3,4,7]
    print(nums)
    
    array = shuffle_array(nums, 3)
    print(array)


if __name__ == '__main__':
    main()
