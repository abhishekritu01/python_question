# check prime number
def is_prime(num):
    if num <=1:
        return False 
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
num = int(input("Enter a number: "))
print(is_prime(num))
