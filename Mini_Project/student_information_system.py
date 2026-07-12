name = input("Enter student name: ")
age = int(input("Enter student age: "))
dep = input("Enter student department: ")
reg = int(input("Enter student register number: "))

m1 = int(input("Enter Maths mark: "))
m2 = int(input("Enter Physics mark: "))
m3 = int(input("Enter Chemistry mark: "))

tot = m1 + m2 + m3
avg = tot / 3
percentage = (tot / 300) * 100

print(f"""
----------- STUDENT DETAILS -----------
Name              : {name}
Age               : {age}
Department        : {dep}
Register Number   : {reg}
Maths Mark        : {m1}
Physics Mark      : {m2}
Chemistry Mark    : {m3}
Total Marks       : {tot}
Average           : {avg}
Percentage        : {percentage:.2f}%
""")

if percentage >= 90:
    print("Grade : A Grade")
elif percentage >= 75:
    print("Grade : B Grade")
elif percentage >= 50:
    print("Grade : C Grade")
elif percentage >= 35:
    print("Grade : D Grade")
else:
    print("Result : Fail")
