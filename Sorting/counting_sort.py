array = [2, 5, 3, 0, 2, 3, 0, 3]

def counting_sort(array):
    size = len(array)

    output = [0] * size
    count = [0] * 10
    for j in range(size):
        count[array[j]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    
    return array

print(counting_sort(array))