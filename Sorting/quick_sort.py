numbers = [ 13, 27, 85, 98, 25, 12, 4, 8, 19, 2, 64, 77, 44, 33,56, 51]


def partition(array, p, r):

    pivot = array[r]  # 4
    i = p - 1  # -1
    for j in range(p, r + 1):
        if array[j] <= pivot:
            i += 1  # 2
            array[i], array[j] = array[j], array[i]
    return i


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)
        print(array)


quick_sort(numbers, 0, 15)
