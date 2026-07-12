# Set Operations in Python

set1 = {"Apple", "Banana", "Mango"}
set2 = {"Banana", "Orange", "Mango"}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("\nUnion:")
print(set1.union(set2))

# Intersection
print("\nIntersection:")
print(set1.intersection(set2))

# Difference
print("\nDifference (Set1 - Set2):")
print(set1.difference(set2))

print("\nDifference (Set2 - Set1):")
print(set2.difference(set1))

# Symmetric Difference
print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))