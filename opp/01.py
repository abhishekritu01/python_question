# class Atm:
    
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.menu()
#         print(id(self))

#     def menu(self):
#         user_input = input(""" 
#                            How would you like to proceed?
#                            1. Enter 1 to create pin
#                            2. Enter 2 to deposit
#                            3. Enter 3 to withdraw
#                            4. Enter 4 to check balance 
#                            5. Enter 5 to exit
                           
#                            """)
        
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()
#         elif user_input == "5":
#             self.exit_program()
#         else:
#             print("Invalid input")

#     def create_pin(self):
#         self.pin = input("Enter your pin: ")
#         print("Pin created successfully")


#     def deposit(self):   
#         temp = input("Enter your pin: ")
#         if temp == self.pin:
#             amount = int(input("Enter the amount: ")) 
#             self.balance = self.balance + amount
#             print("Deposit successful")
#         else:
#             print("Invalid password")


#     def withdraw(self):
#         temp = input("Enter your pin: ")
#         if temp == self.pin:
#             amount = int(input("Enter the amount: ")) 
#             if amount > self.balance:
#                 print("Insufficient balance")
#             else:
#                 self.balance -= amount
#                 print("Withdrawal successful")
#         else:
#             print("Invalid password")     



#     def check_balance(self):
#         temp = input("Enter your pin: ")
#         if temp == self.pin:
#             print("Your balance is:", self.balance)
#         else:
#             print("Invalid password")
            

#     def exit_program(self):
#         exit()


# # Creating an instance of the class
# SBI = Atm()
# SBI.menu()
# # print(id(SBI))




class BankAccount:
    def __init__(self):
        self.pin = None
        self.balance = 0

    def create_pin(self):
        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN created successfully.")
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    def deposit(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.pin:
            amount = float(input("Enter the deposit amount: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Invalid deposit amount. Please enter a positive value.")
        else:
            print("Invalid PIN. Deposit failed.")

    def withdraw(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.pin:
            amount = float(input("Enter the withdrawal amount: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Invalid withdrawal amount. Ensure sufficient balance.")
        else:
            print("Invalid PIN. Withdrawal failed.")

    def check_balance(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return

        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.pin:
            print(f"Your current balance is ${self.balance}.")
        else:
            print("Invalid PIN. Unable to check balance.")

# Example usage:
account = BankAccount()

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
