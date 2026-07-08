# List Methods in Python

# Creating a list
cars = ["Toyota", "Honda", "Hyundai"]

print("Original List:")
print(cars)

# append() - Add item at the end
cars.append("BMW")
print("\nAfter append():")
print(cars)

# insert() - Add item at a specific position
cars.insert(1, "Mercedes")
print("\nAfter insert():")
print(cars)

# remove() - Remove an item by value
cars.remove("Honda")
print("\nAfter remove():")
print(cars)

# pop() - Remove item by index
removed_car = cars.pop(2)
print("\nRemoved Item:", removed_car)
print(cars)

# sort() - Sort the list alphabetically
cars.sort()
print("\nAfter sort():")
print(cars)

# reverse() - Reverse the list
cars.reverse()
print("\nAfter reverse():")
print(cars)

# len() - Count total items
print("\nTotal Cars:", len(cars))