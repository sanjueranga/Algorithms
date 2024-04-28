import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
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
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Counting Sort
def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += 1

    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

# Function to generate random integer arrays
def generate_random_array(length):
    return [random.randint(0, 1000) for _ in range(length)]

# Function to calculate execution time of a sorting algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Function to test a sorting algorithm with different input sizes
def test_sorting_algorithm(sort_func, input_sizes):
    for size in input_sizes:
        arr = generate_random_array(size)
        execution_time = measure_time(sort_func, arr)
        print(f"{sort_func.__name__}({size}): Execution Time = {execution_time:.6f} seconds")

# Test the sorting algorithms
def main():
    input_sizes = [100,500,1000,5000]  # Example input sizes to test with
    sorting_algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, counting_sort]
    for algorithm in sorting_algorithms:
        test_sorting_algorithm(algorithm, input_sizes)

if __name__ == "__main__":
    main()
