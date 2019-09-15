# Account info
current_pin = 3829
current_balance = 500

def change_pin_menu():
    global current_pin
    entered = 0
    while entered == 0:
        try:
            current_pin_selection = int(input("Enter your current PIN code: "))
        except ValueError:
            print("Your entered PIN code is incorrect.")
            continue
        if current_pin != current_pin_selection:
            print("Your entered PIN code is incorrect.")
            continue
        while True:
            try:
                new_pin_selection = int(input("Enter your new PIN code: "))
            except ValueError:
                print("Your entered PIN code is incorrect.")
                continue
            break
        entered = 1
        break
    current_pin = new_pin_selection
    print("\nPIN was changed successfully.\n")
    main_menu()
def deposit_menu():
    global current_balance
    entered = 0
    while entered == 0:
        try:
            deposit_amount = int(input("How much do you want to deposit: "))
        except ValueError:
            print("You have entered incorrect amount.")
            continue
        if deposit_amount < 0:
            print("That's not allowed here.")
            continue
        entered = 1
        break
    current_balance = deposit_amount + current_balance
    print("\nDeposit was successfull.\n")
    main_menu()
def withdraw_menu():
    global current_balance
    entered = 0
    while entered == 0:
        try:
            withdraw_amount = int(input("How much do you want to withdraw: "))
        except ValueError:
            print("You have entered incorrect amount.")
            continue
        if withdraw_amount < 0:
            print("That's not allowed here.")
            continue
        if withdraw_amount > current_balance:
            print("You don't have that much in your balance.")
            continue
        entered = 1
        break
    current_balance = current_balance - withdraw_amount
    print("\nWithdrawal was successfull.\n")
    main_menu()
def show_balance_menu():
    print("\n" + "*************************" + "*" * len(str(current_balance)))
    print(f"Your balance is {current_balance} dollars.")
    print("*************************" + "*" * len(str(current_balance)) + "\n")
    main_menu()
def main_menu():
    print("1 - Withdraw")
    print("2 - Deposit")
    print("3 - Change PIN")
    print("4 - Show your balance")
    print("5 - Logout")
    selected = 0
    while selected == 0:
        try:
            main_choice = int(input("\nEnter your selection: "))
            if (main_choice == 1 or main_choice == 2) or (main_choice == 3 or (main_choice == 4 or main_choice == 5)):
                selected = 1
            else:
                print("Wrong selection. Try again.")
        except ValueError:
            print("Wrong selection. Try again.")
        continue
    if main_choice == 1:
        withdraw_menu()
    elif main_choice == 2:
        deposit_menu()
    elif main_choice == 3:
        change_pin_menu()
    elif main_choice == 4:
        show_balance_menu()
    elif main_choice == 5:
        print("\nYou have logged out.\n")
        login()
def check_pin(pin_input, current_pin):
    if pin_input == current_pin:
        return 1
    else:
        return 0
def login():
    print("Welcome to Niagara Bank.")
    logged_in = 0
    while logged_in == 0:
        try:
            pin_input = int(input("Enter your PIN code: "))
        except ValueError:
            print("You have entered wrong PIN code.")
            continue
        check_pin_result = check_pin(pin_input, current_pin)
        if check_pin_result == 0:
            print("You have entered wrong PIN code.")
        elif check_pin_result == 1:
            print("\nYou have successfully logged in.\n")
            main_menu()
# Start command
login()