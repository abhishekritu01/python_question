
def list_sum(list):
    sum =0
    for i in range(len(list)):
        sum += list[i]

    return sum  

list = [1,2,3,4,5]

print(list_sum(list))