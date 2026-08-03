def calculate_total(m1,m2,m3,m4,m5):
    return m1+m2+m3+m4+m5

def calculate_percentage(total):
    return total/5

def calculate_grade(percentage):
    if percentage >=90:
        return "A" 
    elif percentage >=70:
        return "B" 
    elif percentage >=50:
        return "C" 
    elif percentage >= 35:
        return "D" 
    else:
        return "Fail"
    
def display_result(name,total,percentage,grade):
   print("------ Student Result ------")
   print(f"Name       : {name}")
   print(f"Total      : {total}")
   print(f"Percentage : {percentage}")
   print(f"Grade      : {grade}")


name = input("Enter name: ")

m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))
m4 = int(input("Mark 4: "))
m5 = int(input("Mark 5: "))

total = calculate_total(m1, m2, m3, m4, m5)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)
display_result(name, total, percentage, grade)
