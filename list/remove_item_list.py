
# def remove_and_create_new_list(input_list, to_remove):
#     new_list = [x for x in input_list if x not in to_remove]
#     return new_list

# input_list = [12, 15, 3, 10]
# to_remove = [12, 3]

# result_list = remove_and_create_new_list(input_list, to_remove)

# print(result_list)

# ----------------------------------------------------------------------------------------------

input_list = [12, 15, 3, 10]
to_remove = [12, 3]

result_list = [x for x in input_list if x not in to_remove]
print(result_list)

