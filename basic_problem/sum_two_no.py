
# num1 = 10;
# num2 = 20;

# sum = num1 + num2;

# print("Sum of {0} and {1} is {2}",sum);


#--------------------------by user input

# num1 = input("Enter first number: ");
# num2 = input("Enter second number: ");

# sum = float(num1) + float(num212);

# print("Sum of {0} and {1} is {2}",sum);


#--------------------------by function

# def add_two_no(num1,num2):
#     sum = num1 + num2;
#     return sum;

# num1 = input("Enter first number: ");
# num2 = input("Enter second number: ");

# sum = add_two_no(float(num1),float(num2));

# print("sum of {0} and {1} is {2}",sum);


#--------------------------by function with default value

# def add_two_no(num1=40,num2=20):
#     sum = num1 + num2;
#     return sum;

# sum = add_two_no();
# print("sum of {0} and {1} is {2}",sum);




def add_two_no(a,b=30):
    return a+b;

sum = add_two_no(10);
print("sum of {0} and {1} is {2}",sum);         


#-----------------operator ----------------

num1 = 100;
num2 = 20;

import operator

sum = operator.add(num1,num2);                      
print("sum of {0} and {1} is {2}",sum);


#-------------------------lambda function-------------------

add_two_no = lambda num1,num2: num1+num2;

num1=19;
num2=20;

result = add_two_no(num1,num2);
print("sum of {0} and {1} is {2}",result);


# --------------------using recursion function-------------------

def add_member_result(num1,num2):
    if num2 == 0:
        return num1;
    else:
        return add_member_result(num1+1,num2-1);

num1 = 10;
num2 = 20;

result = add_member_result(num1,num2);
print("sum of {0} and {1} is {2}",result,"using recursion function");