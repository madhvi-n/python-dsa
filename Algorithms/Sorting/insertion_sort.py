"""
Insertion sort
Working:
Assume the first element in the array to be sorted. Store the next element separately in key.
Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.
Now, the first two elements are sorted.
Continue the process till every unsorted element is placed in it's correct position.

Time complexity: O(n^2)
"""

from typing import List


def insertion_sort(num_list: List[int]) -> List[int]:
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1

        while j >= 0 and key < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1

        num_list[j+1] = key
    return num_list


def main():
    num_list = [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
    result = insertion_sort(num_list)
    print(f"Insertion sort: {result}")


if __name__ == '__main__':
    main()


"""
Output:
i=1, key=2: [8, 8, 4, 6, 9, 12, 1, 0, 7, 5]
i=2, key=4: [2, 8, 8, 6, 9, 12, 1, 0, 7, 5]
i=3, key=6: [2, 4, 8, 8, 9, 12, 1, 0, 7, 5]
i=6, key=1: [2, 4, 6, 8, 9, 12, 12, 0, 7, 5]
i=6, key=1: [2, 4, 6, 8, 9, 9, 12, 0, 7, 5]
i=6, key=1: [2, 4, 6, 8, 8, 9, 12, 0, 7, 5]
i=6, key=1: [2, 4, 6, 6, 8, 9, 12, 0, 7, 5]
i=6, key=1: [2, 4, 4, 6, 8, 9, 12, 0, 7, 5]
i=6, key=1: [2, 2, 4, 6, 8, 9, 12, 0, 7, 5]
i=7, key=0: [1, 2, 4, 6, 8, 9, 12, 12, 7, 5]
i=7, key=0: [1, 2, 4, 6, 8, 9, 9, 12, 7, 5]
i=7, key=0: [1, 2, 4, 6, 8, 8, 9, 12, 7, 5]
i=7, key=0: [1, 2, 4, 6, 6, 8, 9, 12, 7, 5]
i=7, key=0: [1, 2, 4, 4, 6, 8, 9, 12, 7, 5]
i=7, key=0: [1, 2, 2, 4, 6, 8, 9, 12, 7, 5]
i=7, key=0: [1, 1, 2, 4, 6, 8, 9, 12, 7, 5]
i=8, key=7: [0, 1, 2, 4, 6, 8, 9, 12, 12, 5]
i=8, key=7: [0, 1, 2, 4, 6, 8, 9, 9, 12, 5]
i=8, key=7: [0, 1, 2, 4, 6, 8, 8, 9, 12, 5]
i=9, key=5: [0, 1, 2, 4, 6, 7, 8, 9, 12, 12]
i=9, key=5: [0, 1, 2, 4, 6, 7, 8, 9, 9, 12]
i=9, key=5: [0, 1, 2, 4, 6, 7, 8, 8, 9, 12]
i=9, key=5: [0, 1, 2, 4, 6, 7, 7, 8, 9, 12]
i=9, key=5: [0, 1, 2, 4, 6, 6, 7, 8, 9, 12]
"""
