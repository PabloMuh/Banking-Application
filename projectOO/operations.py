from auxiliar import *


class account():
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []
        self.bill = []
        self.value = []
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
            print(f"Transfer of {round(value,2)} to account {destine.code} completed successfully.")

    def bills(self):
        if self.bill:
            print(self.bill[0])
            choice = input("Do you want pay the bill? y/n : ")
            if choice == "y":
                value = self.value[0]
                code_bill = input("Enter the surname of bill: ")
            else:
                return
        else:        
            code_bill = input("Enter the bar code of your bill: ")
            value = int(input("Enter the bill value: "))
        if value > self.balance:
            print("You are unable to pay this bill")
            self.bill.append(f"you have a bill of {value} with the bar code {code_bill}")
        else:
            self.balance -= value
            self.balance = round(self.balance, 2)
            print("The bill was successfully paid")
            self.history.append(f"You paid the bill {code_bill}, with the value {value}")
            self.bill.pop(0)
            self.value.pop(0)
    def loan(self):
        loan_value = int(input("How much is the value of loan?"))
        loan_value_after = loan_value * 1.07
        loan_value = round(loan_value,2)
        print(f"if you want to take out this loan, the amount to be paid afterwards will be {loan_value_after}")
        check_loan = input("press y for yes and anything for no: ")
        
        if check_loan == "y":
            self.deposit(loan_value)
            self.bill.append(f"you have a bill of {loan_value_after} with the bank")
            self.value.append(loan_value_after)
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