import os
import time

account_list = []

class account():
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []

    def deposit(self, value):
        self.balance += value
        self.history.append(f"You made a deposit of {value}. Your account balance after this is {self.balance}")
        print(f"you make a deposit of {value} in your account. Your account balance now is {self.balance}")

    def withdraw(self,value):
        if self.balance >= value:
            self.balance = self.balance - value
            self.history.append(f"You realize a withdraw of {value}. Your accout balance after this is {self.balance}")
            print(f"you make a withdraw of {value} in your account. Your account balance now is {self.balance}")
        else:
            print("You are unable to withdraw this value")
    def show_transactions(self):
        for transactions in self.history:
            print(transactions)

    def transfer(self,destine,value):
        if self.balance >= value:
            self.balance -= value
            destine.balance += value
            self.history.append(f"You transferred {value} to account {destine.code}")
            print(f"Transfer of {value} to account {destine.code} completed successfully.")
        else:
            print("You do not have sufficient funds for this transfer.")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def access_account(user):
    while True:
        print("Hello User, Welcome to central administration")
        print("What operation do you want to do?")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - See my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Quit account")
        choice = int(input("Select your choice: "))
        if choice == 1:
            value = int(input("How many is the value of deposit: "))
            user.deposit(value)
        elif choice == 2:
            value = int(input("How many is the value of withdraw: "))
            user.withdraw(value)
        elif choice == 3:
            clear_terminal()
            user.show_transactions()
        elif choice == 4:
            code = input("Enter the account code you want to transfer:")
            check_transfer = False
            for obj in account_list:
                if code == obj.code:
                    check_transfer = True
                    break  
            if check_transfer:
                value = int(input("How much is the value of transfer: "))
                user.transfer(obj, value)
            else:
                print("Account not found, you will be redirected to your home page!!!")
                time.sleep(3)          
                    
        elif choice == 5:
            clear_terminal()
            print(f"Your Current balance is: {user.balance}")
        elif choice == 6:
            clear_terminal()
            break
        else:
            clear_terminal()
            print("Invalid choice, please select another")
        time.sleep(3)
        clear_terminal()


check = True

while True:

    print("Welcome to Metropolitan Bank")
    print("What do you want to do?")
    print("1 - register an account")
    print("2 - access your account")
    print("3 - quit the operation")

    choice = int(input("Type your choice: "))

    if choice == 1:
        clear_terminal()
        code = input("Type your New Code Account(made up of letters and numbers): ")
        password = input("Type your New Password: ")
        check_object = account(code,password)

        while any(check_object.code == obj.code for obj in account_list):
            code = input("This code account already exists, please choose another combination: ")
            check_object = account(code,password)
        account_list.append(check_object)
        print("Account created successfully")
        time.sleep(3)
        clear_terminal()
    elif choice == 2:
        clear_terminal()
        code = input("Type your code account: ")
        password = input("Type your Password: ")
        for obj in account_list:
            if code == obj.code and password == obj.password:
                clear_terminal()
                access_account(obj)
                check = False

        if check:
            print("Account not found, you will be redirected to the home page")
            time.sleep(3)
            clear_terminal()

        check = True
    elif choice == 3:
        clear_terminal()
        print("Thanks for using our services, come back soon!!!")
        break
    else:
        clear_terminal()
        print("invalid operation,select another")