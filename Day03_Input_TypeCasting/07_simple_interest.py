principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))

simple_interest = principal * rate * time / 100
total_amount = principal + simple_interest

print(f"""Simple Interest = {simple_interest}
Total Amount = {total_amount}
""")
