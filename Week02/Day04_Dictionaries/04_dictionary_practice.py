# Dictionary Practice Program

student = {
    "name": "Milind",
    "course": "AIML",
    "semester": 5,
    "marks": 89
}

print("Original Dictionary:")
print(student)

# Add a new key-value pair
student["city"] = "Ghaziabad"

# Update marks
student["marks"] = 95

# Remove course
student.pop("course")

print("\nUpdated Dictionary:")
print(student)

print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

print("\nTotal Items:")
print(len(student))