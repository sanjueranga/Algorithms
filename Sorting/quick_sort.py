numbers = [2, 8, 7, 1, 3, 5, 6, 4]


def partition(array, p, r):

    pivot = array[r] #4
    i = p - 1 #-1
    for j in range(p, r+1):
        if array[j] <= pivot:
            i += 1 #2
            array[i], array[j] = array[j], array[i]
    # array[i + 1], array[r] = array[r], array[i + 1]
    return i


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


quick_sort(numbers, 0, 7)
