"""
Bubble Sort

Working:
Select first element as minimum. Compare minimum with the second element.
If the second element is smaller than minimum, assign the second element as minimum.

Compare minimum with the third element.
Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing.
The process goes on until the last element.

Example:
    Suppose we have the array: (5,3,4,2,1,6).

    First Iteration
        Minimum Element: A[4] = 1
        Swap (A[4], A[0]). The array becomes : (1) (3,4,2,5,6)

    Second Iteration
        Minimum Element: A[3] = 2
        Swap (A[3], A[1]). The array becomes : (1,2) (4,3,5,6)

    Third Iteration
        Minimum Element: A[3] = 3
        Swap (A[3], A[2]). The array becomes : (1,2,3) (4,5,6)

    Fourth Iteration
        Minimum Element: A[3] = 4
        Swap (A[3], A[3]). The array becomes : (1,2,3,4) (5,6)

    Fifth Iteration
        Minimum Element: A[4] = 5
        Swap (A[4], A[4]). The array becomes : (1,2,3,4,5) (6)

    The last element is already sorted. We get the sorted array as : (1,2,3,4,5,6)

Time complexity: O(n^2)
Space complexity: O(1)
"""
from typing import List


def selection_sort(num_list: List[int]) -> List[int]:
    for step in range(0, len(num_list)):
        min_index = step
        for index in range(step + 1, len(num_list)):
            if num_list[index] < num_list[min_index]:
                min_index = index
        num_list[step], num_list[min_index] = num_list[min_index], num_list[step]
    return num_list


def main():
    num_list = [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
    result = selection_sort(num_list)
    print(f"Selection sort: {result}")


if __name__ == '__main__':
    main()
