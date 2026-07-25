def mark_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

result = mark_average(mark1, mark2, mark3)

print("Average =", result)
