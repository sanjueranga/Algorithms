array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
a =  [14,4,7,2,8,1]

def heapify(arr, n, i):
    largest = i #1
    l = 2 * i + 1 #3
    r = 2 * i + 2 #4
    if l < n and arr[i] < arr[l]:
        largest = l 
    if r < n and arr[largest] < arr[r]:
        largest = r #4
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # array = [14,8,7,2,4,1]
        # largest = 4
        # heapify(arr,n,4)
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        print(array)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


print(heapSort(array))
