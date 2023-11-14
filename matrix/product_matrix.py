
# A =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # for i in range(len(A)):
# #     for j in range(len(A[0])):
# #         print(f"{A[i][j]} ", end="")
# #     print() 

# sum = 1

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         sum = sum * A[i][j]
#     print(f"{sum} ", end="")



# Original list
original_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
total_product = 1
for sublist in original_list:
    for num in sublist: 
        total_product = total_product * num

print(f"The total element product in lists is: {total_product}")
