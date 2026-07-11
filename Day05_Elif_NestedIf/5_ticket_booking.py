age = int(input("Enter your age: "))
payment = input("Is payment completed? (yes/no): ").lower()

if age >= 18:
    if payment == "yes":
        print("Ticket Booked")
    else:
        print("Complete Payment")
else:
    print("Not Eligible to Book")
