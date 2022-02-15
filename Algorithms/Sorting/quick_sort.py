"""
Quicksort is a sorting algorithm based on the divide and conquer approach where

1. An array is divided into subarrays by selecting a pivot element (element selected from the array).
While dividing the array, the pivot element should be positioned in such a way that
elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

2. The left and right subarrays are also divided using the same approach.
This process continues until each subarray contains a single element.

3. At this point, elements are already sorted. Finally, elements are combined to form a sorted array
"""
from typing import List

# function to find the partition position
def partition(arr:List[int], low: int, high: int) -> int:

  # choose the rightmost element as pivot
  pivot = arr[high]

  # pointer for greater element
  i = low - 1

  # compare each element with pivot
  for j in range(low, high):
    if arr[j] <= pivot:
      # if element smaller than pivot is found, swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (arr[i], arr[j]) = (arr[j], arr[i])

  # swap the pivot element with the greater element specified by i
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

  # return the position from where partition is done
  return i + 1


def quick_sort(array, low, high) -> None:
  if low < high:

    # find pivot element such that element smaller than pivot are on the left
    # element greater than pivot are on the right
    mid = partition(array, low, high)

    # recursive call on the left of pivot
    quick_sort(array, low, mid - 1)

    # recursive call on the right of pivot
    quick_sort(array, mid + 1, high)


def main():
    arr = [8,7,2,1,5,4,6,3]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == '__main__':
    main()
