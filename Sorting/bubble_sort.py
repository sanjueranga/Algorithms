array = [77, 42, 35, 12, 101, 5]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
        print(array)

bubble_sort(array)
