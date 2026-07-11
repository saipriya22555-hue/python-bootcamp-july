used_units = int(input("Enter units used: "))

if used_units <= 100:
    bill = used_units * 2
elif used_units <= 200:
    bill = used_units * 3
else:
    bill = used_units * 5

print(f"Bill: ₹{bill}")
