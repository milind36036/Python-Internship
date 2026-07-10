# Tuple Practice Program

students = ("Milind", "Rahul", "Aman", "Priya", "Rahul")

print("Student Tuple:")
print(students)

# First student
print("\nFirst Student:")
print(students[0])

# Last student
print("\nLast Student:")
print(students[-1])

# Total students
print("\nTotal Students:")
print(len(students))

# Count Rahul
print("\nRahul appears:")
print(students.count("Rahul"), "times")

# Find index of Aman
print("\nIndex of Aman:")
print(students.index("Aman"))

# Loop through the tuple
print("\nStudent List:")

for student in students:
    print(student)

# Loop with index
print("\nStudents with Index:")

for index, student in enumerate(students):
    print(index, "-", student)