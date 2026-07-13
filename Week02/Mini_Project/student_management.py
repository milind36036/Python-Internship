import csv
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "students.csv")


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RollNo", "Name", "Marks"])


# Show all students
def show_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) == 1:
        print("\nNo student records found.")
        return

    print("\n===== STUDENT LIST =====")
    print("{:<10} {:<20} {:<10}".format("RollNo", "Name", "Marks"))
    print("-" * 40)

    for row in rows[1:]:
        print("{:<10} {:<20} {:<10}".format(row[0], row[1], row[2]))


# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    # Check duplicate roll number
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == roll:
                print("Roll number already exists.")
                return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully.")


# Search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == roll:
                print("\nStudent Found")
                print("Roll No :", row[0])
                print("Name    :", row[1])
                print("Marks   :", row[2])
                return

    print("Student not found.")


# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    students = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        found = False

        for row in reader:
            if row[0] == roll:
                found = True
            else:
                students.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(students)

        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Main Program
create_file()

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Show Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid choice.")