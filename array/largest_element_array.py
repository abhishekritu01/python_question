
# def largest(array,n):
#     array.sort()
#     return array[n-1]

# arr = [10, 324, 45, 90, 9808]
# n = len(arr)
# Ans = largest(arr, n)
# print("Largest in given array ", Ans)


# ------------------- using operator -------------------


import operator 

array = [2,3,5,6,10]
max =0

for i in array:
    if operator.gt(i,max):
        max = i

print('the biggest number' , max)        
