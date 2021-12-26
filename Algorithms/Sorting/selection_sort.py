"""
Bubble Sort

Working:
Select first element as minimum
Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.
Compare minimum with the third element.
Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing.
The process goes on until the last element.

Time Complexity: O(n^2)
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


"""
How it works:
step:0, index=1, minimum is at index=0: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=2, minimum is at index=1: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=3, minimum is at index=1: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=4, minimum is at index=1: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=5, minimum is at index=1: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=6, minimum is at index=1: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=7, minimum is at index=6: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=8, minimum is at index=7: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
step:0, index=9, minimum is at index=7: [8, 2, 4, 6, 9, 12, 1, 0, 7, 5]
Swap 1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]

step:1, index=2, minimum is at index=1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=3, minimum is at index=1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=4, minimum is at index=1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=5, minimum is at index=1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=6, minimum is at index=1: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=7, minimum is at index=6: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=8, minimum is at index=6: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
step:1, index=9, minimum is at index=6: [0, 2, 4, 6, 9, 12, 1, 8, 7, 5]
Swap 2: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]

step:2, index=3, minimum is at index=2: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=4, minimum is at index=2: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=5, minimum is at index=2: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=6, minimum is at index=2: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=7, minimum is at index=6: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=8, minimum is at index=6: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
step:2, index=9, minimum is at index=6: [0, 1, 4, 6, 9, 12, 2, 8, 7, 5]
Swap 3: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]

step:3, index=4, minimum is at index=3: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
step:3, index=5, minimum is at index=3: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
step:3, index=6, minimum is at index=3: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
step:3, index=7, minimum is at index=6: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
step:3, index=8, minimum is at index=6: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
step:3, index=9, minimum is at index=6: [0, 1, 2, 6, 9, 12, 4, 8, 7, 5]
Swap 4: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]

step:4, index=5, minimum is at index=4: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]
step:4, index=6, minimum is at index=4: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]
step:4, index=7, minimum is at index=6: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]
step:4, index=8, minimum is at index=6: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]
step:4, index=9, minimum is at index=6: [0, 1, 2, 4, 9, 12, 6, 8, 7, 5]
Swap 5: [0, 1, 2, 4, 5, 12, 6, 8, 7, 9]

step:5, index=6, minimum is at index=5: [0, 1, 2, 4, 5, 12, 6, 8, 7, 9]
step:5, index=7, minimum is at index=6: [0, 1, 2, 4, 5, 12, 6, 8, 7, 9]
step:5, index=8, minimum is at index=6: [0, 1, 2, 4, 5, 12, 6, 8, 7, 9]
step:5, index=9, minimum is at index=6: [0, 1, 2, 4, 5, 12, 6, 8, 7, 9]
Swap 6: [0, 1, 2, 4, 5, 6, 12, 8, 7, 9]

step:6, index=7, minimum is at index=6: [0, 1, 2, 4, 5, 6, 12, 8, 7, 9]
step:6, index=8, minimum is at index=7: [0, 1, 2, 4, 5, 6, 12, 8, 7, 9]
step:6, index=9, minimum is at index=8: [0, 1, 2, 4, 5, 6, 12, 8, 7, 9]
Swap 7: [0, 1, 2, 4, 5, 6, 7, 8, 12, 9]

step:7, index=8, minimum is at index=7: [0, 1, 2, 4, 5, 6, 7, 8, 12, 9]
step:7, index=9, minimum is at index=7: [0, 1, 2, 4, 5, 6, 7, 8, 12, 9]
Swap 8: [0, 1, 2, 4, 5, 6, 7, 8, 12, 9]

step:8, index=9, minimum is at index=8: [0, 1, 2, 4, 5, 6, 7, 8, 12, 9]
Swap 9: [0, 1, 2, 4, 5, 6, 7, 8, 9, 12]
"""
