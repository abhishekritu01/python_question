
# def fabionaci(num):
#     if num < 2:
#         return num
#     else:
#         return fabionaci(num - 1) + fabionaci(num - 2)
    
# for i in range(5):
#     print(fabionaci(i))





# def fabionaci(num):
#     if num <=1 :
#         return num
#     else:
#         return fabionaci(num - 1) + fabionaci(num - 2)
    
# for i in range(5):
#     print(fabionaci(i), end=',')


# ------------------------------------------------------------------------

# def fib(num):
#     a = 0
#     b = 1

#     if num == 0:
#         return a
#     elif num == 1:
#         return b
#     else:
#         for i in range(2, num + 1):
#             c = a + b
#             a = b
#             b = c
#         return c

# for i in range(5):
#     print(fib(i), end=',')



# -------------------------check number is fibonaci or not


def is_perfect_square(number):
    sqrt_num = int(number**0.5)
    return sqrt_num * sqrt_num == number

def is_fibonacci_recursive(number):
    if number < 0:
        return False
    if number == 0 or number == 1:
        return True
    if not is_perfect_square(5 * number * number + 4) and not is_perfect_square(5 * number * number - 4):
        return False
    return True

# Input a number from the user
try:
    number = int(input("Enter a number: "))
    if is_fibonacci_recursive(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is not a Fibonacci number.")
except ValueError:
    print("Please enter a valid integer.")
 