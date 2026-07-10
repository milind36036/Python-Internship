# Looping Through Tuples

# Creating a tuple
cars = ("BMW", "Audi", "Mercedes", "Toyota", "Honda")

print("Printing all cars:")

# Method 1 - Simple for loop
for car in cars:
    print(car)

print("\nPrinting with index:")

# Method 2 - Using range() and len()
for i in range(len(cars)):
    print("Index", i, ":", cars[i])

print("\nPrinting using enumerate():")

# Method 3 - Using enumerate()
for index, car in enumerate(cars):
    print(index, "-", car)