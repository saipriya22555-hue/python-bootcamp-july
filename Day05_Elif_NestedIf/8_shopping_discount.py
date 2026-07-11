og_amt = int(input("Enter purchased amount: "))

if og_amt >= 5000:
    discount = og_amt * 20 / 100
elif og_amt >= 2000:
    discount = og_amt * 10 / 100
else:
    discount = 0

final_amt = og_amt - discount

print(f"""Original Amount : {og_amt}
Discount : {discount}
Final Amount : {final_amt}""")
