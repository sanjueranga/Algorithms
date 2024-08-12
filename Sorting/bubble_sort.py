array = [56, 51, 13, 33,25, 12, 4, 8, 19, 2, 64, 77, 85, 98,44, 27]


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
        print(array)


print(bubble_sort(array))
