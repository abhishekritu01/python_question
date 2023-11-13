
# def even_number(list):
#     for i in range(len(list)):
#         if list[i] % 2 == 0:
#             print(list[i])

# list = [1,2,3,4,5,6,7,8,9,10]

# print(even_number(list))



# def odd_number(list):
#     for i in range(len(list)):
#         if list[i] % 2 != 0:
#             print(list[i])

# list = [1,2,3,4,5,6,7,8,9,10]

# print(odd_number(list))



# ------- in range

def even_number(list,start,end):
    for i in range(start,end):
        if list[i] % 2 == 0:
            print(list[i])


list = [1,2,3,4,5,6,7,8,9,10]
start =4
end =8

print(even_number(list,start,end))
