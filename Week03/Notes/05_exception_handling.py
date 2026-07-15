# WEEK 3 - EXCEPTION HANDLING

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program finished")