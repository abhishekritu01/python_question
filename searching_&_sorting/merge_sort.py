def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # recursive call on each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_array.append(left[i])
            i += 1
        else:
            result_array.append(right[j])
            j += 1
    
    # Append the remaining elements from both lists
    result_array.extend(left[i:])
    result_array.extend(right[j:])

    return result_array


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
