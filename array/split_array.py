# def array_splitArr(arr,n,k):
#     for i in range(0,k):
#         x=arr[0]
#         # print(x,'x')
#         for j in range(0,n-1):
#             arr[j]=arr[j+1]

#         arr[n-1]=x

# arr = [12, 10, 5, 6, 52, 36]
# n =len(arr)
# position = 3

# array_splitArr(arr,n,position)

# for i in range(0,n):
#     print(arr[i],end=' ')


# ---------------------------------

arr = [12, 10, 5, 6, 52, 36]
n =len(arr)
position = 3

x=arr[:position]
y=arr[position:]

y.extend(x)

for i in range(0,n):
    print(y[i],end=' ')
