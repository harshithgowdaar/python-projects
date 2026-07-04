def menu():
    print("\n---Banking System---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"New Balance: ₹{self.__balance}")


# Create object
b1 = BankAccount()

while True:
    menu()

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        b1.get_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        b1.deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        b1.withdraw(amount)

    elif choice == 4:
        print("Thank you for using the Banking System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")