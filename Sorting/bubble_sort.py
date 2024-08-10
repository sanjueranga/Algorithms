array = [5, 42, 35, 12, 77, 101]


def bubble_sort(array):
    k = 0
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(1, n):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                swapped = True

        if not swapped:
            return array


print(bubble_sort(array))
