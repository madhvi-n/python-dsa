"""
Steps:
1. If the size of array A is 1, then the array is already sorted. So, return.

2. Else, perform one pass of iterative bubble sort on the given subarray.

It will place the last element at its correct position.
3. Use recursion call to perform the above steps again on a smaller subarray with size reduced by one.

Example:
Suppose we have the array: (5,3,4,2,1). We will sort it using the bubble sort algorithm.
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

Time complexity:
Average and Worst case: O(n * n)
Best case: O(n)
"""


def bubble_sort(arr, end_index):
    if end_index == 1:
        return
    for i in range(end_index):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort(arr, end_index - 1)


def main():
    num_list = [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
    print(num_list)
    bubble_sort(num_list, len(num_list) - 1)
    print(f"Bubble sort: {num_list}")


if __name__ == '__main__':
    main()
