pin = int(input("Enter PIN: "))
amount = int(input("Enter the amount:"))
balance = 5000

if pin == 2211:
    if balance >= amount:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
