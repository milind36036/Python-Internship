# Set Practice

# Create a set
cities = {"Delhi", "Mumbai", "Chennai"}

print("Original Set:")
print(cities)

# Add one city
cities.add("Kolkata")
print("\nAfter Adding Kolkata:")
print(cities)

# Add multiple cities
cities.update(["Pune", "Hyderabad"])
print("\nAfter Updating:")
print(cities)

# Remove Mumbai
cities.remove("Mumbai")
print("\nAfter Removing Mumbai:")
print(cities)

# Total number of cities
print("\nTotal Cities:")
print(len(cities))

# Create another set
metro = {"Delhi", "Bengaluru", "Hyderabad"}

print("\nMetro Cities:")
print(metro)

# Union
print("\nUnion:")
print(cities.union(metro))

# Intersection
print("\nIntersection:")
print(cities.intersection(metro))

# Difference
print("\nDifference (Cities - Metro):")
print(cities.difference(metro))

# Symmetric Difference
print("\nSymmetric Difference:")
print(cities.symmetric_difference(metro))