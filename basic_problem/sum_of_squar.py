
def sum_of_square(num):
    sum=0

    for i in range(1, num+1):
        sum = sum + i**2
    return sum

print(sum_of_square(7))



def sum_of_cube(num):
    sum=0
    for i in range(1, num+1):
        sum = sum + i**3
    return sum

print(sum_of_cube(7))