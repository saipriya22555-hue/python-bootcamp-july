a = int(input("Enter 1st subject mark: "))
b = int(input("Enter 2nd subject mark: "))
c = int(input("Enter 3rd subject mark: "))

total = a + b + c
average = total / 3

print("Total =", total)
print("Average =", average)

if average >= 90:
    print("Outstanding")
elif average >= 75:
    print("First Class")
elif average >= 50:
    print("Pass")
else:
    print("Fail")
