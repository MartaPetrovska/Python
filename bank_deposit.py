balance = 20
print("Welcome to our bank.")

while True:
    action = input("Please choose what you would like to do: 1 - Deposit money, 2 - Withdraw money, 3 - Check balance, 4 - Exit: ")

    if action == '1':
        try:
            deposit = int(input("How much do you want to deposit?: "))
            balance += deposit 
            print(f"Your current balance is {balance}")
        except:
            print('You need to input an integer!')
            continue

    elif action == '2':
        try:
            withdraw = int(input("How much do you want to withdraw?: "))
            if withdraw <= balance:
                print(f"You have withdrawn {withdraw} EUR")
                balance -= withdraw
                print(f"Your current balance is {balance} EUR")
            else:
                print(f"There is not enough money in your bank account. Your current balance is {balance}")
        except:
            print('You need to input an integer!')
            continue

    elif action == '3':
        print(f"Your current balance is {balance} EUR")

    elif action == '4':
        print("Thank you for choosing our bank!")
        break

    else:
        print("Invalid option, please choose again.")

    other_action = input("Do you want to do another action? yes/no: ")
    if other_action.lower() == 'no':
        print("Thank you for choosing our bank!")
        break
