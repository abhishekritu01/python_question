

# def smallest_number_in_list(list):
#     list.sort()

#     return list[0]

# list = [1,2,3,4,5]
# print(smallest_number_in_list(list))




# -----------using min function----------------

# def smallest_number_in_list(list):
#     return min(list)


# list  = [11,2,3,4,5,1]
# print(min(list))


# -----------------using loop------------------

# def smallest_number_in_list(list):
#     smallest = list[0]
#     for i in range(len(list)):
#         if list[i] < smallest:
#             smallest = list[i]

#     return smallest

# list = [11,2,3,4,5]

# print(smallest_number_in_list(list))


# -----------------using loop------------------

def smallest_number_in_list(list):
    for i in range(len(list)):
        if list[i] < list[0]:
            list[0] = list[i]

    return list[0]  

list = [11,2,3,4,5]

print(smallest_number_in_list(list))