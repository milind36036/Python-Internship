# JSON File Handling

import json

student = {
    "name": "Milind",
    "course": "AIML",
    "semester": 5,
    "marks": 89
}

# Write JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")

# Read JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print(data)