import random
import time

# BubbleSort

def bubbleSort(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    start_time = time.time()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            break
    
    end_time = time.time()
    print("Bubble_Sort \t\t", end_time - start_time)


# insertionSort

def insertionSort(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    start_time = time.time()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    end_time = time.time()
    print("Insertion_Sort \t\t", end_time - start_time)


# SelectionSort

def selectionSort(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    start_time = time.time()
    n = len(arr)

    for i in range(n-1):
        min_ind = i

        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    end_time = time.time()
    print("Selection_Sort \t\t", end_time - start_time)


# heapSort

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    start_time = time.time()
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    end_time = time.time()
    print("Heap_Sort \t\t", end_time - start_time)


# mergeSort
def mergeSortInit(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    start_time = time.time()
    mergeSort(arr)
    end_time = time.time()
    print("Merge_Sort \t\t", end_time - start_time)
    
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
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

# QuickSort

def quickSortInit(numofelts):
    arr = [random.randint(0, 1000) for _ in range(numofelts)]
    size = len(arr)
    start_time = time.time()
    quickSort(arr, 0, size - 1)
    end_time = time.time()
    print("Quick_Sort \t\t", end_time - start_time)

def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

def partition(array, p, r):
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[r]) = (array[r], array[i + 1])
    return i + 1

def algorithmRunningTimeCalculator(numofelts):
    print("\n*************************************************************")
    print("Algorithmn \t\t Running_Time at", numofelts, "elements")
    bubbleSort(numofelts)
    insertionSort(numofelts)
    selectionSort(numofelts)
    heapSort(numofelts)
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    print("*************************************************************")

# for 100000 elements bubble, insertion, and selection Sort takes a long time 
def algorithmRunningTimeCalculator_100000(numofelts):
    print("\n*************************************************************")
    print("Algorithmn \t\t Running_Time at", numofelts, "elements")
    heapSort(numofelts)
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    print("*************************************************************")

algorithmRunningTimeCalculator(10)
algorithmRunningTimeCalculator(100)
algorithmRunningTimeCalculator(1000)
algorithmRunningTimeCalculator(10000)
algorithmRunningTimeCalculator_100000(100000) 
