# Contact Book using Dictionary

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to update: ")

        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if len(contacts) == 0:
            print("Contact book is empty.")
        else:
            print("\nContact List:")

            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "6":
        print("Contact Book closed.")
        break

    else:
        print("Invalid choice.")