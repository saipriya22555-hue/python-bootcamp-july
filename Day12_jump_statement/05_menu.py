while True:
    print(f"""
====== Calculator ======
1. Addition
2. Subtraction
3. Exit
""")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference =", a - b)
    elif choice == 3:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
