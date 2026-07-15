class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed successfully")
        else:
            print("Book not found")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book is not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)


library = Library()

# Some books already available in the library
library.books = [
    "Python Basics",
    "Machine Learning",
    "Artificial Intelligence"
]

while True:

    print("\n--- Library Management System ---")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book = input("Enter book name to add: ")
        library.add_book(book)

    elif choice == "3":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "4":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "5":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "6":
        print("Exiting Library Management System")
        break

    else:
        print("Invalid choice. Please try again.")