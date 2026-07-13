
m1 = int(input("Enter 1st mark:"))
m2 = int(input("Enter 2nd mark:"))
m3 = int(input("Enter 3rd mark:"))
m4 = int(input("Enter 4th mark:"))
m5 = int(input("Enter 5th mark:"))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 500 * 100

print(f"""Total of five Subjects : {total}
Percentage : {percentage}%""")
