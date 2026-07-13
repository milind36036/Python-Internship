import json

try:
    with open("student.json", "r") as file:
        student = json.load(file)

    print("===== STUDENT DETAILS =====")
    print("Name   :", student["name"])
    print("Age    :", student["age"])
    print("Course :", student["course"])
    print("City   :", student["city"])

except FileNotFoundError:
    print("student.json file not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")