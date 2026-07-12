# Set Methods in Python

# Creating a set
fruits = {"Apple", "Banana", "Mango"}

print("Original Set:")
print(fruits)

# add() - Adds one item
fruits.add("Orange")
print("\nAfter add():")
print(fruits)

# update() - Adds multiple items
fruits.update(["Grapes", "Pineapple"])
print("\nAfter update():")
print(fruits)

# remove() - Removes an item
fruits.remove("Banana")
print("\nAfter remove():")
print(fruits)

# discard() - Removes an item (does not give an error if not found)
fruits.discard("Watermelon")
print("\nAfter discard():")
print(fruits)

# pop() - Removes a random item
removed_item = fruits.pop()
print("\nRemoved Item:", removed_item)
print(fruits)

# len() - Counts total items
print("\nTotal Fruits:", len(fruits))