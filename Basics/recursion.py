"""
Sum of a sequence using recursion
"""
from typing import List


def sum_of_array(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + sum_of_array(arr[1:])


def main():
    result = sum_of_array([1, 2, 3, 4, 5, 12, 18])
    print(result)


if __name__ == '__main__':
    main()
