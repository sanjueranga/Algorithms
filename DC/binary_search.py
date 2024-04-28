array = [3, 6, 7, 11, 32, 33, 53]


def binary_search(array, target, low, high):
    if high >= low:
        mid = (low + high) // 2

        if array[mid] == target:
            print("Element found:", array[mid])
            return mid

        if target < array[mid]:
            print("Searching in the left half...")
            return binary_search(array, target, low, mid - 1)
        else:
            print("Searching in the right half...")
            return binary_search(array, target, mid + 1, high)
    else:
        print("Element not found.")
        return -1


# Example usage
target = 3
result = binary_search(array, target, 0, len(array) - 1)
print("Index of the element:", result)
