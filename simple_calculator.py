def calculator():
    print("Simple Calculator\n")
    print("Select operation:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print()

    choice = int(input("Select choice (1/2/3/4): "))
    print()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print()

    if choice==1:
        print(f"Sum of {num1} and {num2} is: {num1+num2}")
    elif choice==2:
        print(f"Difference of {num1} and {num2} is: {num1-num2}")
    elif choice==3:
        print(f"Product of {num1} and {num2} is: {num1*num2}")
    elif choice==4:
        print(f"Division of {num1} and {num2} is: {num1/num2}")
    else:
        print("Invalid choice!!!")

calculator()