"""
Consider an array arr of distinct numbers sorted in increasing order.
Given that this array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
"""


def find_rotations(arr: list):
    min_val = arr[0]
    n = len(arr)
    min_index = -1

    for i in range(0, n):
        if min_val > arr[i]:
            min_val = arr[i]
            min_index = i
    return min_index


def main():
    print(find_rotations([15, 18, 2, 3, 6, 12]))
    print(find_rotations([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
