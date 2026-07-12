# Looping Through Dictionaries

student = {
    "name": "Milind",
    "course": "AIML",
    "semester": 5,
    "marks": 89
}

print("Student Dictionary:")
print(student)

print("\nPrinting Keys:")

# Print only keys
for key in student:
    print(key)

print("\nPrinting Values:")

# Print only values
for value in student.values():
    print(value)

print("\nPrinting Keys and Values:")

# Print both keys and values
for key, value in student.items():
    print(key, ":", value)