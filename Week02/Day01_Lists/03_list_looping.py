# Looping Through Lists in Python

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Printing all fruits:")

# Using a for loop
for fruit in fruits:
    print(fruit)

print("\nPrinting with index:")

# Using range() and len()
for i in range(len(fruits)):
    print("Index", i, ":", fruits[i])

print("\nPrinting using enumerate():")

# Using enumerate() to get both index and value
for index, fruit in enumerate(fruits):
    print(index, "-", fruit)