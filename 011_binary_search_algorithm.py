def binary_search(array, key, low, high):
    if (low >= high):
        return None
    else:
        mid = low + (high - low) // 2
        if (key == array[mid]):
            return mid
        elif (key > array[mid]):
            return binary_search(array, key, mid + 1, high)
        else:
            return binary_search(array, key, low, mid - 1)


usortedArray = [14, 2, 43, 6, 34, 7, 8, 78, 34, 10, 20, 11, 54, 61, 9, 10]

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

result = binary_search(sortedArray, 15, 0, len(sortedArray) - 1)
print(result)
