
# def left_rotate_array(start,end,arr):
#     temp =arr[start]
#     for i in range(start,end):
#         arr[i] = arr[i+1]
#     arr[end] = temp


# def left_rotate(arr,rotate):
#     for i in range(rotate):
#         left_rotate_array(0,len(arr)-1,arr)

# arr = [1,2,3,4,5,6,7]
# d = 3
# left_rotate(arr,d)
# print(arr)

# =====================================================
# def left_rotate_array(arr,start,end):
#     temp =arr[start]
#     for i in range(start,end):
#         arr[i] = arr[i+1]
#     arr[end] = temp


# def left_rotate(arr,rotate):
#     for i in range (rotate):
#        left_rotate_array(arr,0,len(arr)-1)

# arr = [1,2,3,4,5,6,7]
# rotate = 3

# left_rotate(arr,rotate)

# print(arr)

# ----------------------

def reverseArray(arr,d):
    c=(arr[d:])+(arr[:d])
    return c

arr = [12, 10, 5, 6, 52, 36]
d=3

print(reverseArray(arr,d))
