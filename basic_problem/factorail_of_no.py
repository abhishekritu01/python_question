
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# n = int(input("Enter a number: "))

# print(factorial(n));


# using iteration 

# def factorial(n):
#     if n < 0:
#         return 0;
#     elif n == 0 or n == 1:
#         return 1;
#     else:
#         fact = 1;
#         while(n > 1):
#             fact = fact * n;
#             n = n - 1;
#         return fact;

# n = int(input("Enter a number: "))
# print(factorial(n));

#-------------------------------------------- using for loop

# def factorial(n):
#     if n < 0:
#         return 0;
#     elif n == 0 or n == 1:
#         return 1;
#     else:
#         fact = 1;
#         for i in range(1,n+1):
#             fact = fact * i;
#         return fact;
# n = int(input("Enter a number: "))
# print(factorial(n));


import math

def factorial(n):
    return(math.factorial(n));

n = int(input("Enter a number: "))
print(factorial(n));                       

