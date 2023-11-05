
# def simple_intrest(p,r,t):
#     return (p*r*t)/100;

# p =  int(input("enter the principle amount:"));
# r = int(input("enter the rate of intrest:"));
# t =  int(input("enter the time period:"));

# si = simple_intrest(p,r,t);
# print("simple intrest of {0} and {1} is {2}",si);   



# --------------for compound intrest----------------

def compound_intrest(p,r,t):
    return p*(pow((1+r/100),t));

p =  int(input("enter the principle amount:"));
r = int(input("enter the rate of intrest:"));
t =  int(input("enter the time period:"));

ci = compound_intrest(p,r,t);

print("compound intrest of {0} and {1} is {2}",ci);