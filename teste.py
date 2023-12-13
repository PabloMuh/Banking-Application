import os
import time
import requests

account_list = []

class account():
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []
        self.currency = 1

    def deposit(self, value):
        self.balance += value
        self.balance = round(self.balance, 2)
        self.history.append(f"You made a deposit of {value}. Your account balance after this is {self.balance}")
        print(f"you make a deposit of {value} in your account. Your account balance now is {self.balance}")

    def withdraw(self,value):
        if self.balance >= value:
            self.balance = self.balance - value
            self.balance = round(self.balance, 2)
            self.history.append(f"You realize a withdraw of {value}. Your accout balance after this is {self.balance}")
            print(f"you make a withdraw of {value} in your account. Your account balance now is {self.balance}")
        else:
            print("You are unable to withdraw this value")

    def show_transactions(self):
        for transactions in self.history:
            print(transactions)

    def transfer(self,destine,value,original):
            self.balance -= original
            self.balance = round(self.balance, 2)
            destine.balance += value
            destine.balance = round(destine.balance, 2)
            self.history.append(f"You transferred {value} to account {destine.code}")
            destine.history.append(f"You received {value} of the account {self.code}")
            print(f"Transfer of {value} to account {destine.code} completed successfully.")

    def bills(self):
        code_bill = input("Enter the bar code of your bill: ")
        value = int(input("Enter the bill value: "))
        if value > self.balance:
            print("You are unable to pay this bill")
        else:
            self.balance -= value
            self.balance = round(self.balance, 2)
            print("The bill was successfully paid")
            self.history.append(f"You paid the bill {code_bill}, with the value {value}")
    def loan(self):
        loan_value = int(input("How much is the value of loan?"))
        loan_value_after = loan_value * 1.07
        loan_value = round(loan_value,2)
        print(f"if you want to take out this loan, the amount to be paid afterwards will be {loan_value_after}")
        check_loan = input("press y for yes and anything for no: ")
        
        if check_loan == "y":
            self.deposit(loan_value)
        else:
            clear_terminal()
            print("The Loan was reffused, you will be redirected to the central") 
            time.sleep(3)
            clear_terminal()
    def convert(self):
        clear_terminal()
        print("1 - Real")
        print("2 - Dollar")
        print("3 - Euro")
        select = int(input("Enter your choice:"))
        if select == 2 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'USD') 
            self.currency = 2        
        elif select == 3 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'EUR')  
            self.currency = 3
        elif select == 1 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'BRL') 
            self.currency = 1
        elif select == 1 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'BRL')     
            self.currency = 1
        elif select == 2 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'USD') 
            self.currency = 1
        elif select == 3 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'EUR') 
            self.currency = 1
        else:
            print("You already have this money currency")

        self.history.append("you convert your money")
        self.balance = round(self.balance, 2)
        time.sleep(3)

def convert_currency(amount, base_currency, target_currency):
    api_key = 'YOUR_EXCHANGE_RATE_API_KEY'
    endpoint = f'https://open.er-api.com/v6/latest/{base_currency}'
    
    params = {'apikey': api_key}
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)
        if rate is not None:
            converted_amount = amount * rate
            return converted_amount
        else:
            print(f"Exchange rate not available for {target_currency}.")
    else:
        print(f"Failed to fetch exchange rate. Status code: {response.status_code}")
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Now you have Downloaded the cheque book")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def support():
    choice = int(input("select the number of the operation you have doubt: "))
    clear_terminal()
    if choice == 1:
        print("You chose to make a deposit.")

    elif choice == 2:
        print("You chose to make a withdrawal.")

    elif choice == 3:
        print("You chose to see your transaction history.")

    elif choice == 4:
        print("You chose to make a transfer to another account of this bank.")

    elif choice == 5:
        print("You chose to see your current balance.")

    elif choice == 6:
        print("You chose to request a checkbook.")

    elif choice == 7:
        print("You chose to pay bills.")

    elif choice == 8:
        print("You chose to convert your money to another currency.")

    elif choice == 9:
        print("you chose to make aloan on the bank.")

    else:
        print("Invalid choice, please select another")

    time.sleep(3)

def access_account(user):
    while True:
        print("Hello User, Welcome to central administration")
        print("What operation do you want to do?")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - See my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Request a check book")
        print("7 - Pay bills")
        print("8 - Convert my money to another currency")
        print("9 - loan")
        print("10 - Quit account")

        choice = int(input("Select your choice: "))

        if choice == 1:
            clear_terminal()
            value = int(input("How many is the value of deposit: "))
            user.deposit(value)

        elif choice == 2:
            clear_terminal()
            value = int(input("How many is the value of withdraw: "))
            user.withdraw(value)

        elif choice == 3:
            clear_terminal()
            user.show_transactions()

        elif choice == 4:
            clear_terminal()
            code = input("Enter the account code you want to transfer:")
            check_transfer = False
            for obj in account_list:
                if code == obj.code:
                    check_transfer = True
                    break  

            if check_transfer:
                original = int(input("How much is the value of transfer: "))
                if original <= user.balance:
                    if user.currency == 1 and obj.currency == 2:
                        value = convert_currency(user.balance, 'BRL', 'USD')
                    elif user.currency == 1 and obj.currency == 3:
                        value = convert_currency(user.balance, 'BRL', 'EUR')
                    elif user.currency == 2 and obj.currency == 1: 
                        value = convert_currency(user.balance, 'USD', 'BRL')
                    elif user.currency == 2 and obj.currency == 3:
                        value = convert_currency(user.balance, 'USD', 'EUR')
                    elif user.currency == 3 and obj.currency == 1:
                        value = convert_currency(user.balance, 'EUR', 'BRL')
                    elif user.currency == 3 and obj.currency == 2:
                        value = convert_currency(user.balance, 'EUR', 'USD')
                    user.transfer(obj, value,original)
                else:
                    print("You do not have sufficient funds for this transfer.")          
            else:
                clear_terminal()
                print("Account not found, you will be redirected to your home page!!!")
                time.sleep(3)          
                clear_terminal()    

        elif choice == 5:
            clear_terminal()
            if user.currency == 1:
                print(f"Your Current balance is: {user.balance} reais")
            elif user.currency == 2:
                print(f"Your Current balance is: {user.balance} dollars")
            elif user.currency == 3:
                print(f"Your Current balance is: {user.balance} euros")

        elif choice == 6:
            clear_terminal()
            download_file(url,filename)

        elif choice == 7:
            clear_terminal()
            user.bills()
        elif choice == 8:
            user.convert()
        elif choice == 9:
            user.loan()

        elif choice == 10:
            clear_terminal()
            break

        else:
            clear_terminal()
            print("Invalid choice, please select another")
        time.sleep(3)
        clear_terminal()


# Example usage:
url = 'https://static.vecteezy.com/system/resources/thumbnails/004/566/136/small/bank-check-cheque-template-free-vector.jpg'
filename = 'cheque.jpg'


check = True

while True:
    clear_terminal()
    print("Welcome to Metropolitan Bank")
    print("What do you want to do?")
    print("1 - register an account")
    print("2 - access your account")
    print("3 - support about the operations")
    print("4 - quit the operation")

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
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - See my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Request a check book")
        print("7 - Pay bills")
        print("8 - Convert my money to another currency")
        print("9 - loan")
        support()
    elif choice == 4:
        clear_terminal()
        print("Thanks for using our services, come back soon!!!")
        break
    else:
        clear_terminal()
        print("invalid operation,select another")