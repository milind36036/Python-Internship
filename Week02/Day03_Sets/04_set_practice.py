# Set Practice Program

students = {"Milind", "Rahul", "Aman"}

print("Original Set:")
print(students)

# Add one student
students.add("Priya")
print("\nAfter Adding Priya:")
print(students)

# Add multiple students
students.update(["Karan", "Riya"])
print("\nAfter Updating:")
print(students)

# Remove a student
students.remove("Rahul")
print("\nAfter Removing Rahul:")
print(students)

# Discard a student (No error if not found)
students.discard("Rohit")
print("\nAfter Discarding Rohit:")
print(students)

# Total students
print("\nTotal Students:")
print(len(students))

# Another set
new_students = {"Priya", "Riya", "Ankit"}

print("\nNew Students:")
print(new_students)

# Union
print("\nUnion:")
print(students.union(new_students))

# Intersection
print("\nIntersection:")
print(students.intersection(new_students))

# Difference
print("\nDifference (Students - New Students):")
print(students.difference(new_students))

# Symmetric Difference
print("\nSymmetric Difference:")
print(students.symmetric_difference(new_students))
