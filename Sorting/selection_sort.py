array = [27, 74, 5, 11, 17, 3, 62, 44, 31, 77]


def selection_sort(array):
    for i in range(len(array) - 1):
        key = array[i]

        min_index = i+1
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if array[min_index] < key:
            array[i] = array[min_index]
            array[min_index] = key

    print(array)
            


selection_sort(array)
