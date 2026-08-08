numbers = (10, 20, 10, 30, 10, 40)

number = int(input("Enter the number: "))

count = 0

for i in numbers:
    if i == number:
        count = count + 1

print("Count:", count)
