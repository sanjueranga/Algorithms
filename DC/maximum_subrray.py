array = [-10, 5, 3, -4, 2, -3, 7, 1, 2, -5]


def max_cross_sum(array, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum


def maximum_subarray_sum(array, low, high):
    if low == high:
        return array[low]

    mid = (low + high) // 2

    left_sum = maximum_subarray_sum(array, low, mid)
    right_sum = maximum_subarray_sum(array, mid + 1, high)
    cross_sum = max_cross_sum(array, low, mid, high)

    return max(left_sum, right_sum, cross_sum)


print(maximum_subarray_sum(array, 0, len(array) - 1))
