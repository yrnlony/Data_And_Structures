# Built-in list (dynamic arrays)
arr = [1, 2, 3, 4, 5]

# ----------------------------
# Linear Search (unsorted or sorted arrays)
# ----------------------------
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # return the index where target is found
    return -1  # target not found

# Example usage
print(linear_search(arr, 3))  # Output: 2

# ----------------------------
# Binary Search (requires sorted array)
# ----------------------------
def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # target not found

# Example usage
print(binary_search(arr, 4))  # Output: 3

# ----------------------------
# Insertion Sort (sorts an array in ascending order)
# ----------------------------
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array  # optional, for easier use

# Example usage
unsorted_arr = [5, 2, 4, 1, 3]
sorted_arr = insertion_sort(unsorted_arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]

# ----------------------------
# Binary Deletion (delete an element from a sorted array)
# ----------------------------
def binary_delete(array, target):
    index = binary_search(array, target)
    if index != -1:
        del array[index]
    return array

# Example usage
arr_to_delete = [1, 2, 3, 4, 5]
arr_after_delete = binary_delete(arr_to_delete, 3)
print(arr_after_delete)  # Output: [1, 2, 4, 5]