try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError

    print("Your age is:", age)

except ValueError:
    print("Please enter a valid age")

finally:
    print("Program finished")