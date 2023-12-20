
# pass by referance 
# class Customer:
#     def __init__(self, name):
#         self.name = name


# def greet(customer):
#     print(f"Hello {customer.name}!")    

# cust = Customer('John')

# greet(cust)



# ------------------------------------------------------

#  a = 10 ,b =a
# class Customer:
#     def __init__(self, name):
#         self.name = name


# def greet(customer):
#     print(id(customer), 'customer')


# cust = Customer('John')
# print(id(cust), 'cust')

# greet(cust)



# ------------------------------------------------------



class Customer:
    def __init__(self, name):
        self.name = name


def greet(customer):
    print(id(customer), 'customer')
    print(f"Hello {customer.name}!")
    print(id(customer), 'customer1')
    customer.name = 'abhishek'
    print(id(customer), 'customer2')


cust = Customer('John')

greet(cust)


# class ke object are also mutable list , dictionary , set  