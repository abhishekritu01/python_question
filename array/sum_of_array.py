
# def _sum_of_array(arr):
#     sum = 0
#     for i in arr:
#         sum = sum + i
#     return sum

# arr = [1,2,3,4,5]

# print(_sum_of_array(arr))

# ----------------------------sum of array 
# arr = [1,2,3,4,5]
# ans = sum(arr)
# print(ans)


# ----------------------------sum of array using recursion

def _sum_of_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + _sum_of_array(arr[1:])
    
arr = [1,2,3,4,5]

print(_sum_of_array(arr))