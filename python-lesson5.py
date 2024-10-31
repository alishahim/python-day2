
def display_menu():
    print("Select an option:")
    print("1. Greet")
    print("2. Calculate sum of two numbers")
    print("3. Quit")
while True:
    display_menu()
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("The sum is:", num1 + num2)
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")