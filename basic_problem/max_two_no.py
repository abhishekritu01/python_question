
# find max of two numbers

# num1 = 10;
# num2 = 20;

# if num1 > num2:
#     print("num1 is greater than num2");
# else:
#     print("num2 is greater than num1");


#--------------------------by function with default value

# def max_two_no(a,b):
#     if a > b:
#         return a;
#     else:
#         return b;

# max = max_two_no(10,20);
# print("max of {0} and {1} is {2}",max);


#-----------------operator ----------------

# num1 = 10;
# num2 = 20;

# import operator

# max = operator.gt(num1,num2);
# print("max of {0} and {1} is {2}",max,"using operator");


#-------------------------lambda function-------------------

max_two_no =lambda a,b :a if a>b else b;
print("max of {0} and {1} is {2}",max_two_no(10,20),"using lambda function");    


# --------------------using recursion function-------------------
def max_two_no(a,b):
    if a > b:
        return a;
    else:
        return b;

max = max_two_no(10,20);
print("max of {0} and {1} is {2}",max,"using recursion function");


# by sort function 

a=10; b=20;
list = [a,b];
list.sort();
print(list[-1],"sort function")

   