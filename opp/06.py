class BankAccount:


    # static class variable -----> # static class variable is a variable which is common for all the objects and it is also a constant variable

    counter = 0  # class variable -----> # class variable is a variable which is common for all the objects


    def __init__(self):

        # instance variable--------> # instance variable is a variable which is unique for every object
    
        # encapsulation -----> # encapsulation is a process of binding data and methods together in a class so that no one can access it directly
        self.__pin = None
        self.__balance = 0
        self.__pin =""
        self.__counter = 0
        BankAccount.counter += 1

    def create_pin(self):
        if self.__pin is not None:
            existing_pin_attempt = input("Enter your existing PIN to confirm identity: ")
            if existing_pin_attempt == self.__pin:
                print("Identity confirmed. You can now create a new PIN.")
            else:
                print("Invalid existing PIN. Identity not confirmed.")
                return

        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN created successfully.")
        else:
            print("Invalid PIN. Please enter a 4-digit number.")



    def deposit(self):
        if self.__pin is None:
            print("Please create a PIN first.")
            self.create_pin()  # Prompt the user to create a PIN
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.__pin:
            amount = float(input("Enter the deposit amount: "))
            if amount > 0:
                self.__balance += amount
                print(f"Deposit of ${amount} successful. New balance: ${self.__balance}")
            else:
                print("Invalid deposit amount. Please enter a positive value.")
        else:
            print("Invalid PIN. Deposit failed.")




    def withdraw(self):
        if self.__pin is None:
            print("Please create a PIN first.")
            self.create_pin()  # Prompt the user to create a PIN
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.__pin:
            amount = float(input("Enter the withdrawal amount: "))
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.__balance}")
            else:
                print("Invalid withdrawal amount. Ensure sufficient balance.")
        else:
            print("Invalid PIN. Withdrawal failed.")


    def check_balance(self):
        if self.__pin is None:
            print("Please create a PIN first.")
            self.create_pin()  # Prompt the user to create a PIN
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.__pin:
            print(f"Your current balance is ${self.__balance}.")
        else:
            print("Invalid PIN. Unable to check balance.")


    def set_pin(self, pin):
        self.__pin = pin  

    def get_pin(self):
        return self.__pin         


# Main part of the code
    
# Referance variable -----> # referance variable is a variable which is used to refer an object   ex : account = BankAccount() here account is a referance variable

account = BankAccount()
print(id(account), 'account')

account.__pin = '1234'

while True:
    print("""
    How would you like to proceed?
    1. Enter 1 to create pin
    2. Enter 2 to deposit
    3. Enter 3 to withdraw
    4. Enter 4 to check balance
    5. Enter 5 to exit
    """)

    choice = input()

    if choice == "1":
        account.create_pin()
    elif choice == "2":
        account.deposit()
    elif choice == "3":
        account.withdraw()
    elif choice == "4":
        account.check_balance()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

