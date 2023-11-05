def is_armstrong(num):
    sum = 0
    temp = str(num)
    for i in temp:
        sum += int(i) ** len(temp)
    if sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
print(is_armstrong(num))


