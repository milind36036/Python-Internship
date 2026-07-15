import pandas as pd

data = pd.read_csv("Week03/Notes/students.csv")

print("Student Data:")
print(data)

print("\nAverage Marks:")
print(data["Marks"].mean())

print("\nHighest Marks:")
print(data["Marks"].max())