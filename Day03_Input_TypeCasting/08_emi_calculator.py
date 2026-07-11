loan_amount = float(input("Enter Loan Amount: "))
months = float(input("Enter Number of Months: "))

emi = loan_amount / months

print(f"Monthly EMI = {emi}")
