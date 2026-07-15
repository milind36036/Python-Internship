class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"


calculator = Calculator()

while True:

    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", calculator.add(num1, num2))

        elif choice == "2":
            print("Result:", calculator.subtract(num1, num2))

        elif choice == "3":
            print("Result:", calculator.multiply(num1, num2))

        elif choice == "4":
            print("Result:", calculator.divide(num1, num2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers")