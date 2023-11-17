
# def binarySearch(arr,left,right,target):
#     if left > right:
#         return -1
#     else:
#         mid = int((left+right)//2)
#         if target  == arr[mid]:
#             return mid
#         elif target < arr[mid]:
#             return binarySearch(arr,left,mid-1,target)
#         else:
#             return binarySearch(arr,mid+1,right,target)
# arr = [1,2,3,4,5,6,7,8,9,10]
# left=0
# right=len(arr)-1
# target = 7

# print(binarySearch(arr,left,right,target))



# ----------------


def binary_search(array, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = 0
right = len(array) - 1
target = 7

print(binary_search(array, left, right, target))
