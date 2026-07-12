try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print("\nAddition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)

except ValueError:
    print("Error: Please enter valid numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("\nProgram Ended.")