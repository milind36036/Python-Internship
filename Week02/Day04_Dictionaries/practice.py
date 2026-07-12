

# Dictionary Practice Program

# Create a dictionary
book = {
    "title": "Python Programming",
    "author": "Guido van Rossum",
    "price": 599
}

# Print complete dictionary
print("Original Dictionary:")
print(book)

# Add publisher
book["publisher"] = "Tech Books"

# Update price
book["price"] = 699

# Remove author
book.pop("author")

# Print updated dictionary
print("\nUpdated Dictionary:")
print(book)

# Print all keys
print("\nKeys:")
for key in book.keys():
    print(key)

# Print all values
print("\nValues:")
for value in book.values():
    print(value)

# Print all key-value pairs
print("\nKey-Value Pairs:")
for key, value in book.items():
    print(key, ":", value)

# Print total number of items
print("\nTotal Items:")
print(len(book))