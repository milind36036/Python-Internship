# Dictionary Methods in Python

# Creating a dictionary
student = {
    "name": "Milind",
    "course": "AIML",
    "marks": 89
}

print("Original Dictionary:")
print(student)

# Add a new key-value pair
student["city"] = "Ghaziabad"
print("\nAfter Adding City:")
print(student)

# Update an existing value
student["marks"] = 95
print("\nAfter Updating Marks:")
print(student)

# Remove an item using pop()
student.pop("course")
print("\nAfter Removing Course:")
print(student)

# Print all keys
print("\nKeys:")
print(student.keys())

# Print all values
print("\nValues:")
print(student.values())

# Print all key-value pairs
print("\nItems:")
print(student.items())

# Total number of items
print("\nTotal Items:")
print(len(student))