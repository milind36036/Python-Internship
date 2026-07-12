try:
    num = int(input("Enter a number: "))
    result = 100 / num

    print(result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Zero is not allowed.")