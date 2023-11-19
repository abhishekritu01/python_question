# def quick_sort(array, low, high):
#     if low < high:
#         pivot = partition(array, low, high)
#         quick_sort(array, low, pivot - 1)
#         quick_sort(array, pivot + 1, high)


# def partition(array, low, high):
#     p = array[low]
#     i = low + 1
#     j = high

#     while True:
#         while i <= j and array[i] <= p:
#             i = i + 1

#         while i <= j and array[j] >= p:
#             j = j - 1

#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#         else:
#             break

#     array[low], array[j] = array[j], array[low]

#     return j

# # Example usage:
# arr = [38, 27, 43, 3, 9, 82, 10]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)












def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print(sorted_arr)
