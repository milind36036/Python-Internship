contacts ={}

while True:
    print("\n---Contact Book ---")
    print("1.Add Contacts")
    print("2.View Contacts")
    print("3.Search Contacts")
    print("4.Delete Contacts")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available")
        else:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        print("Contact Book closed")
        break

    else:
        print("Invalid choice")