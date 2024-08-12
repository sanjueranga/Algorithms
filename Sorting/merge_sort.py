nubmers = [56, 51, 13, 33, 25, 12, 4, 8, 19, 2, 64, 77, 85, 98, 44, 27]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        L = array[mid:]
        R = array[:mid]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        print(array)



merge_sort(nubmers)
