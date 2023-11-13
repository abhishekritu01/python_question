

# def positive_number(list):

#     for i in range(len(list)):
#         if list[i] > 0:
#             print(list[i])

# list = [1,2,3,4,5,-1,-2,-3,-4,-5]
# print(positive_number(list))




# def negative_number(list):


# def negative_number(list):

#     for i in range(len(list)):
#         if list[i] < 0:
#             print(list[i])

# list = [1,2,3,4,5,-1,-2,-3,-4,-5]
# print(negative_number(list))



# Given start and end of a range, write a Python program to print all positive numbers in given range. 

def positive_number(list,start,end):
    for i in range(start,end):
        if list[i] > 0:
            print(list[i])

list = [1,2,3,4,5,-1,-2,-3,-4,-5]

start = 2
end = 7


print(positive_number(list,start,end))