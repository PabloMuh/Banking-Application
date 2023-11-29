import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class account():
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []

    def deposit(self,value):
        self.balance = self.balance + value
        self.history.append(f"You realize a deposit of {value}")

    def withdraw(self,value):
        if self.balance > value:
            self.balance = self.balance - value
            self.history.append(f"You realize a withdraw of {value}")
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
    def operations(self,transaction_type):
        if transaction_type == 1:
            conta.deposit(valor)
            print(f"Depósito de {valor} realizado com sucesso.")
        elif transaction_type == "saque":
            conta.withdraw(valor)
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Tipo de transação inválido. Use 'deposito' ou 'saque'.")


account_list = []
count = 0

while True:

    print("Welcome to Metropolitan Bank")
    print("What do you want to do?")
    print("1 - register an account")
    print("2 - access your account")
    print("3 - quit the operation")

    choice = int(input("Type your choice: "))

    if choice == 1:
        code = input("Type your New Code Account(made up of letters and numbers): ")
        password = input("Type your New Password: ")
        new_object = account(code,password)
        account_list.append(new_object)
        limpar_terminal()
    elif choice == 2:
        code = input("Type your code account: ")
        password = input("Type your New Password: ")
        check_object = account(code,password)
        if any(check_object.__dict__ == obj.__dict__ for obj in account_list):
            limpar_terminal()
        else:
            limpar_terminal()
            print("Account not found")
    elif choice == 3:
        limpar_terminal()
        print("Thanks for using our services, come back soon!!!")
        break
    else:
        limpar_terminal()
        print("invalid operation,select another")