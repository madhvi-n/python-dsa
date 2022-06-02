"""
Counting sort

Steps:
1. Find out the maximum element max and minimum element min inside the array.
2. Initialize an array count of length max-min+1 with all elements set to 0.
3. Initialize an array output of size same as the input array A.
4. Store the count of all elements inside the count array by subtracting min and using the difference as the index.
5. Cumulate the sum of elements inside the count array. The count array now holds the position of
each element in the sorted array.
6. Starting from the end take elements from A and do the following.
7. Compute elements index as count[A[i]-min]-1 and store A[i] in output.
8. Decrease count[A[i]-min] by 1.
9. Store the output elements back to original array A.

Time complexity: O(n + k)
Space complexity: o(n/k)

"""


def counting_sort(arr):
    if not arr:
        return []

    arr_len = len(arr)
    arr_max = max(arr)
    arr_min = min(arr)

    # create the counting array
    counting_arr_length = arr_max + 1 - arr_min
    counting_arr = [0] * counting_arr_length

    # count how much a number appears in the arr
    for number in arr:
        counting_arr[number - arr_min] += 1

    # sum each position with its predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the arr
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # create the output arr
    output = [0] * arr_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(0, arr_len)):
        output[counting_arr[arr[i] - arr_min] - 1] = arr[i]
        counting_arr[arr[i] - arr_min] -= 1

    return output


def counting_sort_string(string):
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


def main():
    nums = [60, 3, 2, 7, 4, 5, 4, 23, 56]
    print(nums)
    print(counting_sort(nums))
    print(counting_sort_string("leetcode"))


if __name__ == '__main__':
    main()
