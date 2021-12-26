"""
Bucket sort

Working:
Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets.
Each bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm.
Finally, the sorted buckets are combined to form a final sorted array.
"""

def bucket_sort(num_list):
    bucket_count = int(max(num_list)  - min(num_list)) + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in num_list:
        bucket_index = int(abs(num) // bucket_count)
        buckets[bucket_index].append(num)
    return  [num for bucket in buckets for num in sorted(bucket)]

def main():
    num_list = [8, 2, 4, 9, -12, 98, 15, 369, 213, 7, 26, 68, 39, -23]
    result = bucket_sort(num_list)
    print(f"Bucket sort: {result}")


if __name__ == '__main__':
    main()


"""
Output:
Index of 8: 0
Index of 2: 0
Index of 4: 0
Index of 9: 0
Index of -12: 0
Index of 98: 2
Index of 15: 0
Index of 369: 10
Index of 213: 5
Index of 7: 0
Index of 26: 0
Index of 68: 1
Index of 39: 1
Index of -23: 0

Buckets: [[8, 2, 4, 9, -12, 15, 7, 26, -23], [68, 39], [98], [], [], [213], [], [], [], [], [369], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

Bucket sort: [-23, -12, 2, 4, 7, 8, 9, 15, 26, 39, 68, 98, 213, 369]
"""
