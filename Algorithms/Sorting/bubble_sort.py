"""
Bubble Sort

Steps:
Start from the pair of the first two elements(A[0] and A[1]), compare their values and, swap them if they are not in the
correct order. Do the same for the next pair (A[1] & A[2]) and move similarly for the rest of the array.
The smallest/largest element is at the last position after this step.

Repeat the above steps (n-2) times for the remaining iterations.
Reduce the array size by one each time as the last element is already sorted.
The smallest/largest element in this iteration moves to the rightmost position.
Step 1 in the above algorithm is also called a pass. To sort an array of size n, n-1 passes are required.

Example:
Suppose we have the array: (5,3,4,2,1).
    First Pass:
        (5 3 4 2 1)	→	(3 5 4 2 1)	(3 < 5 swapped)
        (3 5 4 2 1)	→	(3 4 5 2 1)	(4 < 5 swapped)
        (3 4 5 2 1)	→	(3 4 2 5 1)	(2 < 5 swapped)
        (3 4 2 5 1)	→	(3 4 2 1 5)	(1 < 5 swapped)
    Second Pass:
        (3 4 2 1 5)	→	(3 4 2 1 5)
        (3 4 2 1 5)	→	(3 2 4 1 5)	(2 < 4 swapped)
        (3 2 4 1 5)	→	(3 2 1 4 5)	(1 < 4 swapped)
    Third Pass:
        (3 2 1 4 5)	→	(2 3 1 4 5)	(2 < 3 swapped)
        (2 3 1 4 5)	→	(2 1 3 4 5)	(1 < 3 swapped)
    Fourth Pass:
        (2 1 3 4 5)	→	(1 2 3 4 5)	(1 < 2 swapped)
    We get the sorted array after the fourth pass - (1 2 3 4 5)

Time Complexity: O(n^2)
Space complexity: O(n)
"""
from typing import List


def bubble_sort(num_list: List[int]) -> List[int]:
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


def optimized_bubble_sort(num_list: List[int]) -> List[int]:
    for i in range(0, len(num_list)):
        swapped = False

        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapped = True

        if swapped:
            break

    return num_list


def main():
    num_list = [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
    result1 = bubble_sort(num_list)
    result2 = optimized_bubble_sort(num_list)
    print(f"Bubble sort: {result1}")
    print(f"Bubble sort: {result2}")


if __name__ == '__main__':
    main()
