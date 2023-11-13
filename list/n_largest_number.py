

def n_largest_number(list,n):
    list.sort()
    for i in range(len(list)-n,len(list)):
        print(list[i])

list = [11,2,3,4,5,6,7,8,19,10]
n = 4

n_largest_number(list,n)
        