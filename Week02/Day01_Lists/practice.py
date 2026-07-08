# Shopping Cart CRUD Program

cart = []

while True:
    print("\n========== Shopping Cart ==========")
    print("1. Add Item")
    print("2. Show Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        cart.append(item)
        print(item, "added successfully!")

    elif choice == "2":
        if len(cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("\nItems in Cart:")
            for i, item in enumerate(cart, start=1):
                print(i, item)

    elif choice == "3":
        old_item = input("Enter item to update: ")

        if old_item in cart:
            new_item = input("Enter new item name: ")
            index = cart.index(old_item)
            cart[index] = new_item
            print("Item updated successfully!")
        else:
            print("Item not found.")

    elif choice == "4":
        item = input("Enter item to delete: ")

        if item in cart:
            cart.remove(item)
            print("Item deleted successfully!")
        else:
            print("Item not found.")

    elif choice == "5":
        print("Thank you for using Shopping Cart!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")