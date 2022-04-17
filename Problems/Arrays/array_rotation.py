"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
"""


def rotate(nums, k):
    n = nums[:]

    for j in range(k):
        n.append(n.pop(0))
    return n


def rotate_using_temp(nums, k):
    temp = []
    for j in range(k, len(nums)):
        temp.append(nums[j])

    for i in range(k):
        temp.append(nums[i])
    return temp


def rotate_using_slice(nums, k):
    return nums[k:] + nums[:k]


def main():
    nums = [x for x in range(1, 7)]
    print(rotate(nums, 2))
    print(rotate_using_temp(nums, 2))
    print(rotate_using_slice(nums, 2))


if __name__ == '__main__':
    main()
