class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


Address1 = Address('123 Main St', 'New York', 'NY', '10001')
Customer1 = Customer('John', 25, Address1)


print(Customer1.address.street)

