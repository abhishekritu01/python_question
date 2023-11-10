
# The original input is: [12, 35, 9, 56, 24]
# The output after swap first and last is: [24, 35, 9, 56, 12]


# def swap_list(list):
#     size = len(list)

#     # Swapping
#     temp = list[0]
#     list[0] = list[size - 1]
#     list[size - 1] = temp
#     return list

# list = [12, 35, 9, 56, 24]
# print(swap_list(list))





# -------

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
newList = [12, 35, 9, 56, 24]
print(swapList(newList))