
# count occurane of element 

# def occurance_element(list,element):
#     count =0
#     for i in range(len(list)):
#         if list[i] == element:
#             count +=1
#     return count
        
# list = [1,2,3,4,4,5,6,7,8,9,10]

# element = 4
# print(occurance_element(list,element))



# -----------------using count

def occurance_element(list,element):
    return list.count(element)

list = [1,2,3,4,4,5,6,7,8,9,10,4]
element = 4

print(occurance_element(list,element))