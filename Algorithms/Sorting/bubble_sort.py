"""
Bubble Sort

Working:
Starting from the first index, compare the first and the second element.
If the first element is greater than the second element, they are swapped.
Now, compare the second and the third elements. Swap them if they are not in order.
The above process goes on until the last element

Time Complexity: O(n^2)
"""
from typing import List

def bubbleSort(num_list: List[int]) -> List[int]:
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


def optimizedBubbleSort(num_list: List[int]) -> List[int]:
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
    result1 = bubbleSort(num_list)
    result2 = optimizedBubbleSort(num_list)
    print(f"Bubble sort: {result1}")
    print(f"Bubble sort: {result2}")


if __name__ == '__main__':
    main()


"""
How it works:
i=0, j=0: [2, 8, 4, 6, 9, 12, 1, 0, 7, 5]
i=0, j=1: [2, 4, 8, 6, 9, 12, 1, 0, 7, 5]
i=0, j=2: [2, 4, 6, 8, 9, 12, 1, 0, 7, 5]
i=0, j=5: [2, 4, 6, 8, 9, 1, 12, 0, 7, 5]
i=0, j=6: [2, 4, 6, 8, 9, 1, 0, 12, 7, 5]
i=0, j=7: [2, 4, 6, 8, 9, 1, 0, 7, 12, 5]
i=0, j=8: [2, 4, 6, 8, 9, 1, 0, 7, 5, 12]

i=1, j=4: [2, 4, 6, 8, 1, 9, 0, 7, 5, 12]
i=1, j=5: [2, 4, 6, 8, 1, 0, 9, 7, 5, 12]
i=1, j=6: [2, 4, 6, 8, 1, 0, 7, 9, 5, 12]
i=1, j=7: [2, 4, 6, 8, 1, 0, 7, 5, 9, 12]

i=2, j=3: [2, 4, 6, 1, 8, 0, 7, 5, 9, 12]
i=2, j=4: [2, 4, 6, 1, 0, 8, 7, 5, 9, 12]
i=2, j=5: [2, 4, 6, 1, 0, 7, 8, 5, 9, 12]
i=2, j=6: [2, 4, 6, 1, 0, 7, 5, 8, 9, 12]

i=3, j=2: [2, 4, 1, 6, 0, 7, 5, 8, 9, 12]
i=3, j=3: [2, 4, 1, 0, 6, 7, 5, 8, 9, 12]
i=3, j=5: [2, 4, 1, 0, 6, 5, 7, 8, 9, 12]

i=4, j=1: [2, 1, 4, 0, 6, 5, 7, 8, 9, 12]
i=4, j=2: [2, 1, 0, 4, 6, 5, 7, 8, 9, 12]
i=4, j=4: [2, 1, 0, 4, 5, 6, 7, 8, 9, 12]

i=5, j=0: [1, 2, 0, 4, 5, 6, 7, 8, 9, 12]
i=5, j=1: [1, 0, 2, 4, 5, 6, 7, 8, 9, 12]

i=6, j=0: [0, 1, 2, 4, 5, 6, 7, 8, 9, 12]
"""
