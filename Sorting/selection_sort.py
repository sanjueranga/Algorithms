array = [27, 74, 5, 11, 17, 3, 62, 44, 31, 77]


def selection_sort(array):
    for i in range(len(array) - 1):
        key = array[i]

        min_index = i
        j = i + 1
        for j in range(i, len(array)):
            if array[j] < key:
                key = array[j]
                min_index = j

        array[i], array[min_index] = key, array[i]
        print(array)


selection_sort(array)
