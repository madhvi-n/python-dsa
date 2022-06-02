def heapify(arr: list, n: int, i: int) -> None:
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heap_sort(arr: list) -> None:
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)
        

def main():
    arr = [9, 6, 8, 2, 1, 4, 3]
    print(arr)
    
    heap_sort(arr)
    print(arr)
    

if __name__ == '__main__':
    main()