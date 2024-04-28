array = [27, 74, 5, 11, 17, 3, 62, 44, 31, 77]

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)

selection_sort(array)
