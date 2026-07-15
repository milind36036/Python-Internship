class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal = subtotal + product.total_price()

        return subtotal

    def calculate_tax(self, subtotal):
        tax = subtotal * 0.05
        return tax

    def display_bill(self):
        print("\n----------------------------------------")
        print("              FINAL BILL")
        print("----------------------------------------")
        print("Product\t\tPrice\tQty\tTotal")

        for product in self.products:
            print(
                product.name,
                "\t",
                product.price,
                "\t",
                product.quantity,
                "\t",
                product.total_price()
            )

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        final_amount = subtotal + tax

        print("----------------------------------------")
        print("Subtotal:", subtotal)
        print("Tax (5%):", tax)
        print("Final Amount:", final_amount)
        print("----------------------------------------")


bill = Bill()

while True:

    print("\n--- Billing System ---")
    print("1. Add Product")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            product = Product(name, price, quantity)

            bill.add_product(product)

            print("Product added successfully")

        except ValueError:
            print("Please enter valid price and quantity")

    elif choice == "2":
        if len(bill.products) == 0:
            print("No products added yet")
        else:
            bill.display_bill()

    elif choice == "3":
        print("Billing system closed")
        break

    else:
        print("Invalid choice")