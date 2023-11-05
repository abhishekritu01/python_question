if 5>2 :
    print("Five is greater than two!")
   
if 5>2 :
    print("Five is greater than two!")
    


    #  variable in python --------------------------------------------------------------------------------------------

    x = 5
    y="Hello, World!"
    print(x,y)


    # casting in python ------------------------------------------------------------------------------------------------

# If you want to specify the data type of a variable, this can be done with casting.
    x = str(3)
    y = int(3)
    z = float(3)
    print(x,y,z)

    # get the type -----------------------------------------------------------------------------------------------------
    print(type(x))
    print(type(y))
    print(type(z))

    # Variable names are case-sensitive ------------------------------------------------------------------------------------------
    a = 4
    A = "Sally"
    #A will not overwrite a
    print(a)

    # Multi  words variables Name ------------------------------------------------------------------------------------------
    # Camel Case
    #Pascal Case
    #Snake Case

# Many Values to Multiple Variables ------------------------------------------------------------------------------------------
# Python allows you to assign values to multiple variables in one line:
x,y,z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables ------------------------------------------------------------------------------------------
x = y = z = "Orange"
print(z,"hello")


# Unpack a Collection -----------------------------------------------------------------------------------------------------
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
# print(y)
# print(z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:-------------------------------------

x = 5 
y = "John"
# print(x+y)    


# Global Variables -----------------------------------------------------------------------------------------------------                    
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"
def myfunc():
    print("Python is "+x)
myfunc()



#python data types -----------------------------------------------------------------------------------------------------
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x=5
print(type(x))  



class MyClass:
    x = 5
    def __init__(self, name, age):      #The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age                  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    
    def myfunc(self):           #self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        print("Hello my name is "+self.name)        #It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:          

p1 = MyClass()
print(p1.x)

