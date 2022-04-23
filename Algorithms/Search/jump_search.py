"""
Jump search is an interval searching algorithm.
It is a relatively new algorithm that works only on sorted arrays.
It tries to reduce the number of comparisons required than linear search by not scanning every single element like
linear search. In jump search, the array is divided into m blocks. It searches the element in one block and, if the
element is not present, then moves to the next block. When the algorithm finds the block containing the element,
it uses the linear search algorithm to find the exact index. This algorithm is faster than linear search but slower
than binary search

Steps:
1. Start from the first element set i as 0 and block size m as √n.
2. While A[min(m,n)-1] < X and i < n.
    Set i as m and increment m by √n.
3. If i >= n return -1.

4. While A[i]< X do the following:
    increment i
    if i is equal to min(m,n) return -1
5. If A[i] == X return i.
6. Else return -1.

Example:
Suppose we have the array: (1, 2, 3, 4, 5, 6, 7, 8, 9), and we want to find X - 7.
Since there are 9 elements, we have n as 9.
Set i as 0 and m as √9 that is 3.
A[2] is smaller than X . Set i as 3 and m as 6.
A[5] is smaller than X . Set i as 6 and m as 9.
A[8] is equal to X . Break out of the loop.
i as 6 is less than n.
A[6] == 7 . Break out of the loop
Since A[6] == 7, return 6.


Time complexity: O(sqrt(n))
"""
import math


def jump_search(arr, target):
    length = len(arr)

    # Find block size to be jumped
    step = math.sqrt(length)

    # Find the block where element is present
    prev = 0
    while arr[int(min(step, length) - 1)] < target:
        prev = step
        step += math.sqrt(length)
        if prev >= length:
            return -1

    # Find the element using linear search. Block beginning from prev.
    while arr[int(prev)] < target:
        prev += 1

        if prev == min(step, length):
            return -1

    # Check if element at prev is the same as the target element
    if arr[int(prev)] == target:
        return int(prev)
    return -1


def main():
    print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))


if __name__ == '__main__':
    main()
