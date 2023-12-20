
# collection-- 

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __intro__(self):
        print(f"Hello {self.name}!")    



c1 = Customer('abhishek', 20)
c2 = Customer('abh', 20)
c3 = Customer('hello', 25)


L = [c1, c2, c3]


for i in L:
    print(i.name, i.age)

    

# for i in L:
#     i.__intro__()

