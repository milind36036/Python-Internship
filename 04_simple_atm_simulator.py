pin = "1234"
balance = 10000


def check_balance():
    print("Your balance is ₹", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully")
        print("New balance is ₹", balance)
    else:
        print("Invalid amount")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining balance is ₹", balance)


print("Simple ATM Simulator")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("Login successful")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN")