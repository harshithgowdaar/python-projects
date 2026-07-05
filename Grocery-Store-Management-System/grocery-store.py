class GroceryStore:

    def __init__(self):
        self.items = {
            "salt": 20,
            "sugar": 50,
            "rice": 45,
            "oil": 120,
            "spices": 40,
            "peanut": 92,
            "apple": 200,
            "potato": 30
        }
        self.cart = []

    def menu(self):
        print("\n===== Grocery Store =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Total Price")
        print("5. Exit")

    def show_items(self):
        print("\nAvailable Items:")
        for item in self.items:
            print(f"{item} : ₹{self.items[item]}")

    def add_item(self):
        self.show_items()

        item = input("\nEnter item: ").lower()

        if item in self.items:
            self.cart.append(item)
            print(f"{item} added successfully.")
        else:
            print("Item not available.")

    def remove_item(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
            return

        item = input("Enter item to remove: ").lower()

        if item in self.cart:
            self.cart.remove(item)
            print(f"{item} removed successfully.")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for item in self.cart:
                print(item)

    def total_price(self):
        total = 0

        for item in self.cart:
            total += self.items[item]

        print("Total Price: ₹", total)


store = GroceryStore()

while True:
    store.menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        store.add_item()

    elif choice == "2":
        store.remove_item()

    elif choice == "3":
        store.view_cart()

    elif choice == "4":
        store.total_price()

    elif choice == "5":
        print("Thank you for visiting our store!")
        break

    else:
        print("Invalid choice.")