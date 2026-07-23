import pandas as pd

df = pd.read_csv("Week04/Project/Employee_Data_Analysis/employees.csv")

print("--- Employee Data ---")
print(df)
# Calculate average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count employees in each department
department_count = df["Department"].value_counts()
print("\nDepartment-wise Employee Count:")
print(department_count)
# Filter employees above salary threshold
salary_threshold = 50000

filtered_employees = df[df["Salary"] > salary_threshold]

print("\nEmployees with salary above", salary_threshold)
print(filtered_employees)
# Export filtered results to a new CSV
filtered_employees.to_csv(
    "Week04/Project/Employee_Data_Analysis/filtered_employees.csv",
    index=False
)

print("\nFiltered employee data exported successfully!")