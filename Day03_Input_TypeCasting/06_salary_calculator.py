basic = float(input("Enter Basic Salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100

gross = basic + hra + da

print(f"""Basic Salary = {basic}
HRA = {hra}
DA = {da}
Gross Salary = {gross}
""")
