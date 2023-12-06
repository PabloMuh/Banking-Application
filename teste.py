import os
import time

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
            destine.deposit(value)
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
        print("3 - See the my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Quit account")
        choice = int(input("Select your choice: "))
        if choice == 1:
            value = int(input("How many is the value of deposit: "))
            user[1].deposit(value)
        elif choice == 2:
            value = int(input("How many is the value of withdraw: "))
            user[1].withdraw(value)
        elif choice == 3:
            user[1].show_transactions()
        elif choice == 4:
            for obj in enumerate(account_list):
                if code == obj[1].code:
                    check_transfer = True
            
            code = input("Enter the account code you want to transfer:")
            value = int(input("How many is the value of transference: "))
                    
        elif choice == 5:
            clear_terminal()
            print(f"Your Current balance is: {user[1].balance}")
        elif choice == 6:
            clear_terminal()
            break
        else:
            clear_terminal()
            print("Invalid choice, please select another")
        time.sleep(3)
        clear_terminal()

account_list = []
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
        for obj in enumerate(account_list):
            if code == obj[1].code and password == obj[1].password:
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