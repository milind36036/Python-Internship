class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited:", amount)
        else:
            print("Please enter a valid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)

    def display_balance(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


account1 = BankAccount("Milind Bhatnagar", "1234567890", 5000)

while True:

    print("\n--- Bank Account Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account1.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)

    elif choice == "3":
        account1.display_balance()

    elif choice == "4":
        print("Thank you for using our banking system.")
        break

    else:
        print("Invalid choice. Please try again.")