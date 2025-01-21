print("Welcome to the calculator")
x = input('''1. Enter 1 to start the calculator \n2. Enter any other number to exit the calculator\n''')
y = int (x)
while y == 1:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(x, "+", y, "=", x + y)
    elif choice == 2:
        print(x, "-", y, "=", x - y)
    elif choice == 3:
        print(x, "*", y, "=", x * y)
    elif choice == 4:
        print(x, "/", y, "=", x / y)
    elif choice == 5:
        print(x, "^2", "=", x ** 2)
    elif choice == 6:
        print("sqrt(", x, ")", "=", x ** 0.5)
    elif choice == 7:
        print("Exiting")
        break
else:
    print("Invalid input")