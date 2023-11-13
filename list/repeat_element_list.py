
# def repeat_list(list):
#     repeat_list =[]
#     for i in range(len(list)):
#         k = i+1
#         for j in range(k,len(list)):
#             if list[i] == list[j]:
#                 repeat_list.append(list[i])

#     return repeat_list

# list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]

# print(repeat_list(list))

       


# --------using operators --------------------

import operator as op

list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]

new_list  =[]

for i in list:

    n =op.countOf(list,i)

    if n > 1:
        if op.countOf(new_list,i) == 0:
            new_list.append(i)

print(new_list)

