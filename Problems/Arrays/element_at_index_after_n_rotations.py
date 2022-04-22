"""
Find element at given index after right circular rotations on elements at indices in the ranges[start, end]
"""


# Solution works for rotation of elements at indices in the range by k=1 element
def find_element(arr, ranges, index) -> int:
    for i in range(len(ranges)):
        [start, end] = ranges[i]
        last = arr.pop(end)
        arr.insert(0, last)
        print(arr)
    return arr[index]


def main():
    arr = [1, 2, 3, 4, 5]
    print(find_element(arr, [[0, 2], [0, 3]], 1))


if __name__ == '__main__':
    main()
