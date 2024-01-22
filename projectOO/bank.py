from operations import *

url = 'https://static.vecteezy.com/system/resources/thumbnails/004/566/136/small/bank-check-cheque-template-free-vector.jpg'
filename = 'cheque.jpg'

def access_account(user,account_list):
    while True:
        print("Hello User, Welcome to central administration, What operation do you want to do?")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - See my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Request a check book")
        print("7 - Pay bills")
        print("8 - Convert my money to another currency")
        print("9 - loan")
        print("10 - Investments")
        print("11 - Quit account")

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
            user.transfer(account_list)    

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
            user.investiment()
            
        elif choice == 11:
            clear_terminal()
            break

        else:
            clear_terminal()
            print("Invalid choice, please select another")
        time.sleep(3)
        clear_terminal()