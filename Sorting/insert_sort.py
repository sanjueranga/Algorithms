array = [27, 74, 5, 11, 17, 3, 62, 44, 31, 77]

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        print(key)
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            print(array)

        array[j + 1] = key
        print(array)
    return array

print(insert_sort(array))