from operations import *
import random

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
                        value = convert_currency(original, 'BRL', 'USD')
                    elif user.currency == 1 and obj.currency == 3:
                        value = convert_currency(original, 'BRL', 'EUR')
                    elif user.currency == 2 and obj.currency == 1: 
                        value = convert_currency(original, 'USD', 'BRL')
                    elif user.currency == 2 and obj.currency == 3:
                        value = convert_currency(original, 'USD', 'EUR')
                    elif user.currency == 3 and obj.currency == 1:
                        value = convert_currency(original, 'EUR', 'BRL')
                    elif user.currency == 3 and obj.currency == 2:
                        value = convert_currency(original, 'EUR', 'USD')
                    else:
                        value = original
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
            print("What investiment do you want to do?")
            print("1 - saving")
            print("2 - direct treasure")
            print("3 - stock exchange")

            investiment_choice = int(input("Select the option: "))

            if investiment_choice == 1:
                print(f"with this investiment, you will have {round(user.balance * 1.0826,2)} per year, but zero risks")
                investiment_check = input("want to continue? y/n : ")
                if investiment_check == "y":
                    user.balance = user.balance * 1.0826

            elif investiment_choice == 2:
                print(f"with this investiment, you will have {round(user.balance * 1.1182,2)} per year, but 2% of risks")
                investiment_check = input("want to continue? y/n : ")
                if investiment_check == "y":
                    probability = random.randint(0,100)
                    if probability < 98:
                        user.balance = user.balance * 1.1182                
                    else:
                        user.balance = user.balance * 0.8818

            elif investiment_choice == 3:
                print(f"with this investiment, you will have one impredictable change, high risks, but highs chance earn much money")
                investiment_check = input("want to continue? y/n : ")
                if investiment_check == "y":
                    probability = random.randint(0,200)
                    user.balance = user.balance * (probability / 100)    
                           
            user.balance = round(user.balance,2)
            print(f"after one year, your balance now is {user.balance}")
            time.sleep(3)
            
        elif choice == 11:
            clear_terminal()
            break

        else:
            clear_terminal()
            print("Invalid choice, please select another")
        time.sleep(3)
        clear_terminal()