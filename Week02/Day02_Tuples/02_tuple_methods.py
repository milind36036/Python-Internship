# Tuple Methods in Python

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Apple", "Orange")

print("Original Tuple:")
print(fruits)

# count() - Counts how many times an item appears
apple_count = fruits.count("Apple")
print("\nNumber of Apples:", apple_count)

# index() - Finds the index of the first occurrence
mango_index = fruits.index("Mango")
print("Index of Mango:", mango_index)

# Length of tuple
print("\nTotal Fruits:", len(fruits))