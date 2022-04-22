"""
Given an array of integers, task is to print the array in the order – smallest number, Largest number, 2nd smallest number,
2nd largest number, 3rd smallest number, 3rd largest number and so on…..
"""


def rearrange(arr: list) -> None:
    arr.sort()
    n = len(arr)

    # To store modified array
    temp = [0] * (n + 1)

    # Adding numbers from sorted array to new array accordingly
    index = 0

    # Traverse from begin and end simultaneously
    i = 0
    j = n - 1

    while i <= n // 2 or j > n // 2:
        temp[index] = arr[i]
        index = index + 1

        temp[index] = arr[j]
        index = index + 1
        i, j = i + 1, j - 1

    # Modifying original array
    for i in range(0, n):
        arr[i] = temp[i]

    print(arr)


def main():
    rearrange([5, 8, 1, 4, 2, 9, 3, 7, 6])


if __name__ == '__main__':
    main()
