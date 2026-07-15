import json

file = open("Week03/Notes/student.json", "r")

data = json.load(file)

print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Marks:", data["marks"])

file.close()
