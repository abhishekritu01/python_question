# def is_armstrong(num):
#     sum = 0
#     temp = str(num)
#     for i in temp:
#         sum += int(i) ** len(temp)
#     if sum == num:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))
# print(is_armstrong(num))


# -------- by recursion

def is_armstrong(num):
    if num == 0:
        return 0
    else:
        return (num % 10) ** len(str(num)) + is_armstrong(num // 10)

num = int(input("Enter a number: "))

print(is_armstrong(num))

