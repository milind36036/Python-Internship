# List CRUD Operations

students = []

while True:
    print("\n========== Student List ==========")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for i, student in enumerate(students, start=1):
                print(i, student)

    elif choice == "3":
        old_name = input("Enter student name to update: ")

        if old_name in students:
            new_name = input("Enter new name: ")
            index = students.index(old_name)
            students[index] = new_name
            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")