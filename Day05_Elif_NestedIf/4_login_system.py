username = input("Enter username:").lower()
password = input("Enter password:").lower()

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
