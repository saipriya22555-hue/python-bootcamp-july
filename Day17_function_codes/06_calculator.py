def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Answer =", add(num1, num2))
elif choice == 2:
    print("Answer =", subtract(num1, num2))
elif choice == 3:
    print("Answer =", multiply(num1, num2))
elif choice == 4:
    if num2 != 0:
        print("Answer =", divide(num1, num2))
    else:
        print("Division by zero is not possible.")
else:
    print("Invalid Choice")
