import random
import time


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Quick Sort
def partition(array, p, r):
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


# Counting Sort
def counting_sort(arr):
    size = len(arr)
    max_val = max(arr)
    output = [0] * size
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]

    return arr


# Function to generate random integer arrays
def generate_random_array(length):
    return [random.randint(0, 1000) for _ in range(length)]


# Function to calculate execution time of a sorting algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time


def test_sorting_algorithm(sort_func, input_sizes):
    for size in input_sizes:
        arr = generate_random_array(size)
        if sort_func.__name__ == "quick_sort":
            start_time = time.time()
            sort_func(arr, 0, len(arr) - 1)
            end_time = time.time()
        else:
            start_time = time.time()
            sort_func(arr)
            end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"{sort_func.__name__}({size}): Execution Time = {execution_time:.6f} seconds"
        )


def main():
    input_sizes = [100, 500, 1000, 5000, 10000]
    sorting_algorithms = [
        bubble_sort,
        selection_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
        counting_sort,
    ]
    for algorithm in sorting_algorithms:
        test_sorting_algorithm(algorithm, input_sizes)


if __name__ == "__main__":
    main()
