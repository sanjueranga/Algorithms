def counting_sort(array, exp):
    size = len(array)

    output = [0] * size
    count = [0] * 10
    for j in range(size):
        index = array[j] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

    return array


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10
        print(arr)


array = [329, 457, 657, 839, 436, 720, 355]

radix_sort(array)
