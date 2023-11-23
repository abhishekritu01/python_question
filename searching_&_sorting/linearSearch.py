
# def linearSearch(array,target):
#     for i in range(len(array)):
#         if target == array[i]:
#             return 1
#         else:
#             return 1
        
# array =[12,44,66,72,2,2,5]
# target =22

# print(linearSearch(array,target))


def linear_search_recursion(array,target,index):
    if index ==len(array):
        return False
    if array[index] == target:
        return True
    return linear_search_recursion(array,target,index+1)

array = [12, 44, 66, 72, 2, 2, 5]
index =0
target = 22

print(linear_search_recursion(array,target,index))
    