# Appending Data to a Text File

with open("student.txt", "a") as file:
    file.write("College: ADGIPS\n")
    file.write("Semester: 5\n")

print("Data appended successfully.")