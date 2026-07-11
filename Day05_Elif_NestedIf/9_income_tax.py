income = int(input("Enter income: "))

if income >= 1000000:
    tax = income * 20 / 100
elif income >= 500000:
    tax = income * 10 / 100
else:
    tax = 0

net_income = income - tax

print(f"""Income : {income}
Tax : {tax}
Net Income : {net_income}""")
