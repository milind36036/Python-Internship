try:
    num = int(input("Enter number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Result =", result)

finally:
    print("Program Finished.")
    