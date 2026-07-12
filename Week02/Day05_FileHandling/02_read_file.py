# Reading Data from a Text File

with open("student.txt", "r") as file:
    data = file.read()

print("File Content:")
print(data)