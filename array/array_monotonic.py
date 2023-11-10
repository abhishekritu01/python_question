
# def isMonotonic(array):
#     increasing = decreasing = True

#     for i in range(len(array)-1):
#         if array[i] < array[i+1]:
#             decreasing = False
#         elif array[i] > array[i+1]:
#             increasing = False

#     return increasing or decreasing

# array = [6, 5, 4, 4]
# print(isMonotonic(array))



#----------------------------

def isMonotonic(A):
    return (all(A[i]<=A[i+1] for i in range(len(A)-1)) or
            all(A[i]>=A[i+1] for i in range(len(A)-1)))

A = [6, 5, 4, 4]

print(isMonotonic(A))
