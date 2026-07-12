# Writing Data to a CSV File

import csv

# Data to write
students = [
    ["Name", "Roll No", "Marks"],
    ["Milind", 101, 89],
    ["Rahul", 102, 92],
    ["Priya", 103, 95]
]

# Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write all rows
    writer.writerows(students)

print("CSV file created successfully.")