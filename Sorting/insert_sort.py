array = [4, 3, 2, 5, 1]


def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        # print(key)
        j = i - 1
        # print(array[j])
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            array[j] = key
            # j -= 1
            # print(array)

        array[j + 1] = key
        # print(array)
    return array


print(insert_sort(array))
